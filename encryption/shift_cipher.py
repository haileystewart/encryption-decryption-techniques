# shift_cipher.py
# This script implements the Shift Cipher (Caesar Cipher) for both encryption and decryption.
# It takes in plaintext/ciphertext and a key (shift value), and applies the Caesar shift.

def shift_cipher_encrypt(plaintext, key):
    """
    Encrypt the plaintext using a Caesar cipher with the given shift key.
    :param plaintext: The message to encrypt.
    :param key: The number of positions to shift each letter (integer).
    :return: The encrypted ciphertext.
    """
    encrypted_text = ""
    
    # Loop over each character in the plaintext
    for char in plaintext:
        if char.isalpha():  # Only shift alphabetic characters
            shift = key % 26  # Ensure that the shift is within 26 letters
            base = ord('A') if char.isupper() else ord('a')  # Check if uppercase or lowercase
            # Shift character and wrap around the alphabet
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    
    return encrypted_text

def shift_cipher_decrypt(ciphertext, key):
    """
    Decrypt the ciphertext using a Caesar cipher with the given shift key.
    :param ciphertext: The message to decrypt.
    :param key: The number of positions the letters were shifted by during encryption (integer).
    :return: The decrypted plaintext.
    """
    decrypted_text = ""
    
    # Loop over each character in the ciphertext
    for char in ciphertext:
        if char.isalpha():  # Only shift alphabetic characters
            shift = key % 26  # Ensure that the shift is within 26 letters
            base = ord('A') if char.isupper() else ord('a')  # Check if uppercase or lowercase
            # Shift character backwards and wrap around the alphabet
            decrypted_text += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted_text += char  # Non-alphabetic characters remain unchanged
    
    return decrypted_text
