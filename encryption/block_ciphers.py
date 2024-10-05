# block_ciphers.py
# This script implements block ciphers (AES, DES, 3DES) and supports different modes (ECB, CBC, etc.)
# It handles key generation, padding, and encryption/decryption processes.

from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
from utils.padding import pad, unpad

# AES encryption
def aes_encrypt(plaintext, key, mode='ECB', iv=None):
    # Create cipher object based on mode
    if mode == 'ECB':
        cipher = AES.new(key, AES.MODE_ECB)
    elif mode == 'CBC':
        if iv is None:
            iv = generate_iv(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    elif mode == 'CFB':
        if iv is None:
            iv = generate_iv(AES.block_size)
        cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    elif mode == 'OFB':
        if iv is None:
            iv = generate_iv(AES.block_size)
        cipher = AES.new(key, AES.MODE_OFB, iv=iv)

    # Encrypt the already padded plaintext
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext, iv  # Return ciphertext and IV (if applicable)

# AES decryption
def aes_decrypt(ciphertext, key, mode='ECB', iv=None):
    # Create cipher object based on mode
    if mode == 'ECB':
        cipher = AES.new(key, AES.MODE_ECB)
    elif mode == 'CBC':
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    elif mode == 'CFB':
        cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    elif mode == 'OFB':
        cipher = AES.new(key, AES.MODE_OFB, iv=iv)

    # Decrypt and unpad
    decrypted_bytes = cipher.decrypt(ciphertext)
    decrypted_text = unpad(decrypted_bytes, AES.block_size).decode('utf-8')
    return decrypted_text

# DES encryption
def des_encrypt(plaintext, key, mode='ECB', iv=None):
    # Create cipher object based on mode
    if mode == 'ECB':
        cipher = DES.new(key, DES.MODE_ECB)
    elif mode == 'CBC':
        if iv is None:
            iv = generate_iv(DES.block_size)
        cipher = DES.new(key, DES.MODE_CBC, iv=iv)
    elif mode == 'CFB':
        if iv is None:
            iv = generate_iv(DES.block_size)
        cipher = DES.new(key, DES.MODE_CFB, iv=iv)
    elif mode == 'OFB':
        if iv is None:
            iv = generate_iv(DES.block_size)
        cipher = DES.new(key, DES.MODE_OFB, iv=iv)

    # Encrypt the already padded plaintext
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext, iv  # Return ciphertext and IV (if applicable)

# DES decryption
def des_decrypt(ciphertext, key, mode='ECB', iv=None):
    # Create cipher object based on mode
    if mode == 'ECB':
        cipher = DES.new(key, DES.MODE_ECB)
    elif mode == 'CBC':
        cipher = DES.new(key, DES.MODE_CBC, iv=iv)
    elif mode == 'CFB':
        cipher = DES.new(key, DES.MODE_CFB, iv=iv)
    elif mode == 'OFB':
        cipher = DES.new(key, DES.MODE_OFB, iv=iv)

    # Decrypt and unpad
    decrypted_bytes = cipher.decrypt(ciphertext)
    decrypted_text = unpad(decrypted_bytes, DES.block_size).decode('utf-8')
    return decrypted_text

# AES key generation (128, 192, or 256-bit key)
def generate_aes_key(key_size=128):
    """Generate an AES key. Accepts 128, 192, or 256-bit keys."""
    return get_random_bytes(key_size // 8)

# DES key generation (8 bytes)
def generate_des_key():
    """Generate a DES key (8 bytes)."""
    return get_random_bytes(8)

# IV generation (16 bytes for AES, 8 bytes for DES)
def generate_iv(block_size):
    """Generate an initialization vector (IV) with the specified block size."""
    return get_random_bytes(block_size)
