import os

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.config.config import settings

import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host=settings.database_host,
        user=settings.database_user,
        password=settings.database_password,
        database=settings.database_name,
        port=settings.database_port
    )

MIGRATIONS_TABLE = "migrations"

def ensure_migrations_table(conn):
    cursor = conn.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {MIGRATIONS_TABLE} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            filename VARCHAR(255) NOT NULL UNIQUE,
            executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()

def run_migrations():
    conn = get_connection()
    ensure_migrations_table(conn)

    cursor = conn.cursor()

    # Get applied migrations
    cursor.execute(f"SELECT filename FROM {MIGRATIONS_TABLE}")
    applied = {row[0] for row in cursor.fetchall()}

    migration_path = os.path.join("resources", "database", "migrations")
    migrations = sorted(os.listdir(migration_path))

    for migration in migrations:
        if migration not in applied and migration.endswith(".sql"):
            print(f"Running migration: {migration}")
            with open(os.path.join(migration_path, migration), "r") as f:
                sql = f.read()
                cursor.execute(sql)
            cursor.execute(
                f"INSERT INTO {MIGRATIONS_TABLE} (filename) VALUES (%s)",
                (migration,)
            )
            conn.commit()

    cursor.close()
    conn.close()
    print("✅ All migrations applied.")

if __name__ == "__main__":
    run_migrations()
