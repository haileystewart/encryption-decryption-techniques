# permutation_cipher.py
# This script implements the Permutation Cipher for encryption and decryption.
# It permutes the characters of the plaintext using a defined key or order.

def permutation_encrypt(plaintext, key):
    """
    Encrypt the plaintext using the Permutation Cipher with the given key.
    :param plaintext: The message to encrypt.
    :param key: A list of integers representing the permutation order.
    :return: The encrypted ciphertext.
    """
    # Calculate the size of the block based on the key length
    block_size = len(key)
    ciphertext = []
    
    # Pad the plaintext with spaces to make it a multiple of the block size
    padded_plaintext = plaintext + " " * (block_size - len(plaintext) % block_size)
    
    # Divide the plaintext into blocks of the same size as the key
    for i in range(0, len(padded_plaintext), block_size):
        block = padded_plaintext[i:i + block_size]
        
        # Permute the block according to the key
        permuted_block = ''.join([block[key[j] - 1] for j in range(block_size)])
        ciphertext.append(permuted_block)

    return ''.join(ciphertext)  # Do not remove spaces, as spaces are part of the text


def permutation_decrypt(ciphertext, key):
    """
    Decrypt the ciphertext using the Permutation Cipher with the given key.
    :param ciphertext: The encrypted message to decrypt.
    :param key: A list of integers representing the permutation order.
    :return: The decrypted plaintext.
    """
    # Calculate the size of the block based on the key length
    block_size = len(key)
    plaintext = []
    
    # Reverse the permutation key (to undo the permutation)
    reverse_key = [key.index(i + 1) for i in range(block_size)]

    # Divide the ciphertext into blocks of the same size as the key
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i + block_size]
        
        # Ensure the block is the correct size
        if len(block) < block_size:
            block += " " * (block_size - len(block))

        # Permute the block according to the reverse key
        permuted_block = ''.join([block[reverse_key[j]] for j in range(block_size)])
        plaintext.append(permuted_block)

    return ''.join(plaintext).rstrip()  # Remove padding spaces at the end
