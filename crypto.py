import base64
import hashlib
import os

def get_or_create_key(key_file='.key'):
    key_file = str(key_file)
    if os.path.exists(key_file):
        with open(key_file, 'r') as f:
            return f.read().strip()
    key = base64.b64encode(os.urandom(32)).decode()
    with open(key_file, 'w') as f:
        f.write(key)
    return key

def encrypt(data, key):
    key_bytes = hashlib.sha256(key.encode()).digest()
    data_bytes = data.encode()
    encrypted = bytes(a ^ b for a, b in zip(data_bytes, (key_bytes * (len(data_bytes) // len(key_bytes) + 1))[:len(data_bytes)]))
    return base64.b64encode(encrypted).decode()

def decrypt(data, key):
    key_bytes = hashlib.sha256(key.encode()).digest()
    encrypted = base64.b64decode(data)
    decrypted = bytes(a ^ b for a, b in zip(encrypted, (key_bytes * (len(encrypted) // len(key_bytes) + 1))[:len(encrypted)]))
    return decrypted.decode()
