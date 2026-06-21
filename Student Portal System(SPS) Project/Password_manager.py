import hashlib
import secrets

def generate_salt():
    return secrets.token_hex(16)

def hash_password(password, salt):
    text = password + salt
    return hashlib.sha256(text.encode()).hexdigest()

def verify(stored_hash, entered_password, salt):
    new_hash = hash_password(entered_password, salt)

    return new_hash == stored_hash


def verify_password(stored_hash, entered_password, salt):
    return verify(stored_hash, entered_password, salt)
