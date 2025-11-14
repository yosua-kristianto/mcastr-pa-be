import hmac
from config.config import settings
import hashlib
import base64

def hash(message: str) -> str:
    """Generate hash for given message."""
    mac = hmac.new(settings.secret.encode("utf-8"), message.encode("utf-8"), hashlib.sha512).digest()
    return base64.b64encode(mac).decode("utf-8")

def verify_hash(hash: str, compare: str) -> bool:
    """Compare both hashes. Return true if equal.
    """

    print(f"Hash {hash}")
    print(f"Compare {compare}")

    return hmac.compare_digest(hash, compare)