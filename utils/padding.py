# padding.py
# This script contains padding and unpadding functions for block ciphers.
# It pads the plaintext if it's not a multiple of the block size, ensuring proper encryption.

def pad(plaintext, block_size):
    """
    Pads the plaintext using PKCS#7 padding to ensure it is a multiple of the block size.
    :param plaintext: The plaintext to pad (in bytes).
    :param block_size: The block size to pad to (in bytes).
    :return: The padded plaintext (in bytes).
    """
    padding_needed = block_size - (len(plaintext) % block_size)
    padding = bytes([padding_needed] * padding_needed)  # Create padding in bytes
    return plaintext + padding


def unpad(padded_text, block_size):
    """
    Removes the PKCS#7 padding from the plaintext.
    :param padded_text: The padded plaintext to unpad (in bytes).
    :param block_size: The block size that was used for padding (in bytes).
    :return: The unpadded plaintext (in bytes).
    """
    if len(padded_text) == 0:
        raise ValueError("Padded text cannot be empty.")

    padding_len = padded_text[-1]  # Get the value of the last byte, which indicates padding size

    # Check if the padding length is valid
    if padding_len < 1 or padding_len > block_size:
        raise ValueError("Invalid padding length.")

    # Ensure that all padding bytes are equal to the padding length
    if padded_text[-padding_len:] != bytes([padding_len] * padding_len):
        raise ValueError("Invalid padding bytes.")

    return padded_text[:-padding_len]
