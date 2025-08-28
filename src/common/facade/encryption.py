import hmac
from config.config import settings
import hashlib


def hash(message: str) -> str:
    """Generate hash for given message."""
    return hmac.new(settings.secret.encode("utf-8"), message.encode("utf-8"), hashlib.sha512).hexdigest()

def verify_hash(hash: str, compare: str) -> bool:
    """Compare both hashes. Return true if equal.
    """

    print(f"Hash {hash}")
    print(f"Compare {compare}")

    return hmac.compare_digest(hash, compare)