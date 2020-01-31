# defines helper functions for core and admin purposes

import random
# import secrets
from string import ascii_uppercase

def create_alphanumeric_id(n):
    id = "0" * n

    valid_digits = list(map(str, range(0, 10))) + list(ascii_uppercase)

    for i in range(n):
        id = id[:i] + random.choice(valid_digits) + id[i+1:]

    return id

"""
def secret_code():
    return secrets.token_urlsafe(64)
"""
