# permutation_cipher.py
# This script implements the Permutation Cipher for encryption and decryption.
# It permutes the characters of the plaintext using a defined key or order.

import random
from utils.padding import pad, unpad

def generate_valid_block_size(message_length: int) -> int:
    """
    Generate a valid block size that is a factor of the message length.
    """
    block_sizes = [block_size for block_size in range(2, message_length + 1) if message_length % block_size == 0]
    if not block_sizes:
        return message_length  # Return full length if no factors found
    return random.choice(block_sizes)

def generate_permutation_key(block_size: int) -> list[int]:
    """
    Generate a random permutation key of a specified block size.
    """
    digits = list(range(block_size))
    random.shuffle(digits)
    return digits

def encrypt(message: str, key: list[int] = None, block_size: int = None) -> tuple[str, list[int]]:
    """
    Encrypt a message using a permutation cipher with block rearrangement using a key.
    """
    message = message.upper().replace(" ", "").encode()  # Ensure message is in bytes and uppercase
    message_length = len(message)

    # Default key and block size generation if not provided
    if key is None or block_size is None:
        block_size = generate_valid_block_size(message_length)
        key = generate_permutation_key(block_size)

    # Apply padding using the pad function from padding.py
    padded_message = pad(message, block_size)

    encrypted_message = b""  # Use bytes for concatenation
    for i in range(0, len(padded_message), block_size):
        block = padded_message[i:i + block_size]
        rearranged_block = [block[digit] for digit in key]
        encrypted_message += bytes(rearranged_block)

    return encrypted_message.decode(), key  # Return as string for readability

def decrypt(encrypted_message: str, key: list[int]) -> str:
    """
    Decrypt an encrypted message using a permutation cipher with block rearrangement.
    """
    encrypted_message = encrypted_message.encode()  # Ensure message is in bytes
    key_length = len(key)
    decrypted_message = b""

    for i in range(0, len(encrypted_message), key_length):
        block = encrypted_message[i:i + key_length]
        original_block = [b""] * key_length
        for j, digit in enumerate(key):
            if j < len(block):
                original_block[digit] = block[j]
        decrypted_message += bytes(original_block)

    # Remove padding using the unpad function from padding.py
    return unpad(decrypted_message, key_length).decode()  # Return as string

def main() -> None:
    """
    Driver function to pass message to get encrypted, then decrypted.
    """
    message = "HELLO WORLD"
    encrypted_message, key = encrypt(message)

    decrypted_message = decrypt(encrypted_message, key)
    print(f"Decrypted message: {decrypted_message}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
