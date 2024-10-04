import secrets

# This script contains functions for generating and validating keys for different ciphers.
# This script contains functions for generating and validating keys.
# It ensures that the key length matches the requirements for different ciphers (AES, DES, etc.).

def generate_aes_key(key_size):
    """
    Generates a random AES key of the specified size.
    :param key_size: The size of the AES key (must be 128, 192, or 256 bits).
    :return: A random AES key in bytes.
    """
    if key_size not in [128, 192, 256]:
        raise ValueError("Invalid AES key size. Choose 128, 192, or 256 bits.")
    
    # Convert bits to bytes
    key_bytes = key_size // 8
    return secrets.token_bytes(key_bytes)


def generate_des_key():
    """
    Generates a random DES key (56 bits).
    :return: A random DES key in bytes (8 bytes with parity bits).
    """
    return secrets.token_bytes(8)


def generate_3des_key():
    """
    Generates a random 3DES (Triple DES) key (either 14 or 21 bytes).
    :return: A random 3DES key in bytes.
    """
    # Choose either 112-bit (14 bytes) or 168-bit (21 bytes) key
    key_size = secrets.choice([14, 21])
    return secrets.token_bytes(key_size)


def validate_key(key, expected_length):
    """
    Validates that the provided key is of the expected length.
    :param key: The key to validate (in bytes).
    :param expected_length: The expected length of the key in bytes.
    :return: True if valid, raises ValueError otherwise.
    """
    if len(key) != expected_length:
        raise ValueError(f"Invalid key length. Expected {expected_length} bytes, got {len(key)} bytes.")
    return True
