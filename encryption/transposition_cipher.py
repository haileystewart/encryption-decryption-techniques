# transposition_cipher.py
# This script implements both Simple and Double Transposition Ciphers.
# It rearranges the characters of the plaintext in a new order based on the transposition method.

import math

# Single Transposition Encryption
def transposition_encrypt(message, provided_key):
    cipher = ""

    # Use the provided key
    key = provided_key

    # track key indices
    k_indx = 0

    msg_len = float(len(message))
    msg_lst = list(message)
    key_lst = sorted(list(key))

    # calculate column of the matrix
    col = len(key)

    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))

    # add the padding character '_' in empty
    # the empty cell of the matrix
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)

    # create Matrix and insert message and
    # padding characters row-wise
    matrix = [msg_lst[i: i + col]
              for i in range(0, len(msg_lst), col)]

    # read matrix column-wise using key
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1

    return cipher

# Single Transposition Decryption
def transposition_decrypt(cipher, provided_key):
    message = ""

    # Use the provided key
    key = provided_key

    # track key indices
    k_indx = 0

    # track message indices
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)

    # calculate column of the matrix
    col = len(key)

    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))

    # convert key into list and sort
    # alphabetically so we can access
    # each character by its alphabetical position.
    key_lst = sorted(list(key))

    # create an empty matrix to
    # store deciphered message
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]

    # Arrange the matrix column wise according
    # to permutation order by adding into new matrix
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])

        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1

    # convert decrypted message matrix into a string
    try:
        message = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot handle repeating words.")

    null_count = message.count('_')

    if null_count > 0:
        return message[: -null_count]

    return message

def double_transposition_encrypt(plaintext, first_key, second_key):
    """
    Encrypt the plaintext using a Double Transposition Cipher with two keys.
    """
    print(f"Debug: First Transposition with key1: {first_key}")
    first_pass = transposition_encrypt(plaintext, provided_key=first_key)
    print(f"Debug: Result after first transposition: {first_pass}")

    print(f"Debug: Second Transposition with key2: {second_key}")
    second_pass = transposition_encrypt(first_pass, provided_key=second_key)
    print(f"Debug: Result after second transposition: {second_pass}")

    return second_pass

def double_transposition_decrypt(ciphertext, first_key, second_key):
    """
    Decrypt the ciphertext using a Double Transposition Cipher with two keys.
    """
    print(f"Debug: First Decryption with key2: {second_key}")
    first_pass = transposition_decrypt(ciphertext, provided_key=second_key)
    print(f"Debug: Result after first decryption: {first_pass}")

    print(f"Debug: Second Decryption with key1: {first_key}")
    second_pass = transposition_decrypt(first_pass, provided_key=first_key)
    print(f"Debug: Result after second decryption: {second_pass}")

    return second_pass
