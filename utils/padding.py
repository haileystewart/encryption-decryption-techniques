# padding.py
# This script contains padding and unpadding functions for block ciphers.
# It pads the plaintext if it's not a multiple of the block size, ensuring proper encryption.

def pad(plaintext: bytes, block_size: int) -> bytes:
    """
    Pads the plaintext using PKCS#7 padding to ensure it is a multiple of the block size.
    :param plaintext: The plaintext to pad (in bytes).
    :param block_size: The block size to pad to (in bytes).
    :return: The padded plaintext (in bytes).
    """
    padding_needed = block_size - (len(plaintext) % block_size)
    padding = bytes([padding_needed]) * padding_needed  # Create padding bytes
    return plaintext + padding


def unpad(padded_text: bytes, block_size: int) -> bytes:
    """
    Removes the PKCS#7 padding from the plaintext.
    :param padded_text: The padded plaintext to unpad (in bytes).
    :param block_size: The block size that was used for padding (in bytes).
    :return: The unpadded plaintext (in bytes).
    """
    if len(padded_text) == 0:
        raise ValueError("Padded text cannot be empty.")

    padding_len = padded_text[-1]  # The value of the last byte indicates padding size
    
    # Check if the padding length is valid
    if padding_len < 1 or padding_len > block_size:
        raise ValueError("Invalid padding length.")
    
    # Verify that all padding bytes are equal to the padding length
    padding_bytes = padded_text[-padding_len:]
    if any(pad_byte != padding_len for pad_byte in padding_bytes):
        raise ValueError("Invalid padding bytes.")

    return padded_text[:-padding_len]
