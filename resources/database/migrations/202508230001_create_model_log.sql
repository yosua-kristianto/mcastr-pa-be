CREATE TABLE IF NOT EXISTS mlops_tbl_model_log (
    uuid VARCHAR(36) PRIMARY KEY,
    version_id VARCHAR(60),
    user_session_id TEXT NOT NULL,
    prompt TEXT NOT NULL,
    model_output SMALLINT NOT NULL,
    feedback_actual_output SMALLINT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NULL DEFAULT NULL,
    deleted_at TIMESTAMP NULL DEFAULT NULL,
    CONSTRAINT fk_model_log_version FOREIGN KEY (version_id)
        REFERENCES mlops_tbl_version(model_name)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);