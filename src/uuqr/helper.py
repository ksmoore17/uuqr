"""
defines helper functions for classes
"""

from uuid import uuid4

def create_uuid():
    uuid = uuid4()
    return uuid.hex

"""
def secret_code():
    return secrets.token_urlsafe(64)
"""
