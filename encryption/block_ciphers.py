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
    else:
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    # Pad plaintext and ensure it is in bytes
    padded_plaintext = pad(plaintext.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

# AES decryption
def aes_decrypt(ciphertext, key, mode='ECB', iv=None):
    # Create cipher object based on mode
    if mode == 'ECB':
        cipher = AES.new(key, AES.MODE_ECB)
    else:
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    # Decrypt and unpad
    decrypted_bytes = cipher.decrypt(ciphertext)
    decrypted_text = unpad(decrypted_bytes, AES.block_size).decode('utf-8')
    return decrypted_text

# DES encryption
def des_encrypt(plaintext, key, mode='ECB', iv=None):
    # Create cipher object based on mode
    if mode == 'ECB':
        cipher = DES.new(key, DES.MODE_ECB)
    else:
        cipher = DES.new(key, DES.MODE_CBC, iv=iv)

    # Pad plaintext and ensure it is in bytes
    padded_plaintext = pad(plaintext.encode('utf-8'), DES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

# DES decryption
def des_decrypt(ciphertext, key, mode='ECB', iv=None):
    # Create cipher object based on mode
    if mode == 'ECB':
        cipher = DES.new(key, DES.MODE_ECB)
    else:
        cipher = DES.new(key, DES.MODE_CBC, iv=iv)

    # Decrypt and unpad
    decrypted_bytes = cipher.decrypt(ciphertext)
    decrypted_text = unpad(decrypted_bytes, DES.block_size).decode('utf-8')
    return decrypted_text

# AES key generation (128, 192, or 256-bit key)
def generate_aes_key(length=16):
    """Generate an AES key. Default is 128-bit (16 bytes)."""
    return get_random_bytes(length)

# DES key generation (8 bytes)
def generate_des_key():
    """Generate a DES key (8 bytes)."""
    return get_random_bytes(8)

# IV generation (16 bytes for AES, 8 bytes for DES)
def generate_iv(block_size):
    """Generate an initialization vector (IV) with the specified block size."""
    return get_random_bytes(block_size)
