# transposition_cipher.py
# This script implements both Simple and Double Transposition Ciphers.
# It rearranges the characters of the plaintext in a new order based on the transposition method.

import math
import re
from itertools import chain

# Simple Transposition Cipher Logic
def transposition_encrypt(plaintext, key):
    """
    Encrypt the plaintext using a Columnar Transposition Cipher with a given key.
    """
    plaintext = plaintext.replace(" ", "")  # Remove spaces for simplicity
    msg_len = len(plaintext)
    col = len(key)

    # If the key is larger than the message, return the message unchanged
    if col >= msg_len:
        return plaintext

    encrypted_message = ""
    column = []

    # Form the matrix column-wise based on the key
    for i in range(len(key)):
        column.append(plaintext[i::len(key)])

    # Sort the columns by key and reassemble
    key_dict = {i: key[i] for i in range(len(key))}
    sorted_key = sorted(key_dict.items(), key=lambda pair: pair[1])

    for k in sorted_key:
        encrypted_message += ''.join(column[k[0]])

    return encrypted_message


def transposition_decrypt(ciphertext, key):
    """
    Decrypt the ciphertext using a Columnar Transposition Cipher with a given key.
    """
    msg_len = len(ciphertext)
    col = len(key)

    # If the key is larger than the message, return the message unchanged
    if col >= msg_len:
        return ciphertext

    rows = math.ceil(msg_len / col)
    empty_matrix = [""] * col

    # Sort the key to create the decryption order
    key_dict = {i: key[i] for i in range(len(key))}
    sorted_key = sorted(key_dict.items(), key=lambda pair: pair[1])

    row_pointer = 0
    char_pointer = 0

    for k in sorted_key:
        col_idx = k[0]
        if col_idx >= col - (rows * col - msg_len):  # Handle uneven columns
            max_rows = rows - 1
        else:
            max_rows = rows

        for r in range(max_rows):
            empty_matrix[col_idx] += ciphertext[char_pointer]
            char_pointer += 1

    # Rebuild the message row-wise
    decrypted_message = ''
    for r in range(rows):
        for col in empty_matrix:
            if r < len(col):
                decrypted_message += col[r]

    return decrypted_message


# Double Transposition Cipher Logic
def double_transposition_encrypt(plaintext, first_key, second_key):
    """
    Encrypt the plaintext using a Double Transposition Cipher with two keys.
    """
    first_pass = transposition_encrypt(plaintext, first_key)
    return transposition_encrypt(first_pass, second_key)


def double_transposition_decrypt(ciphertext, first_key, second_key):
    """
    Decrypt the ciphertext using a Double Transposition Cipher with two keys.
    """
    first_pass = transposition_decrypt(ciphertext, second_key)
    return transposition_decrypt(first_pass, first_key)
