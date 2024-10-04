# vigenere_cipher.py
# This script implements the Vigenère Cipher, a polyalphabetic substitution cipher.
# It uses a keyword to apply different Caesar shifts to each letter of the plaintext.

def vigenere_encrypt(plaintext, keyword):
    """
    Encrypt the plaintext using the Vigenère cipher with the given keyword.
    :param plaintext: The message to encrypt.
    :param keyword: The keyword to determine the shifts.
    :return: The encrypted ciphertext.
    """
    encrypted_text = []
    keyword = keyword.upper()
    keyword_length = len(keyword)
    keyword_shifts = [ord(char) - ord('A') for char in keyword]

    keyword_index = 0  # This will keep track of keyword position

    for char in plaintext:
        if char.isalpha():  # Only shift alphabetic characters
            shift = keyword_shifts[keyword_index % keyword_length]
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text.append(encrypted_char)
            keyword_index += 1  # Move to the next keyword letter only for alphabetic characters
        else:
            encrypted_text.append(char)  # Non-alphabetic characters remain unchanged

    return ''.join(encrypted_text)


def vigenere_decrypt(ciphertext, keyword):
    """
    Decrypt the ciphertext using the Vigenère cipher with the given keyword.
    :param ciphertext: The encrypted message to decrypt.
    :param keyword: The keyword to determine the shifts.
    :return: The decrypted plaintext.
    """
    decrypted_text = []
    keyword = keyword.upper()
    keyword_length = len(keyword)
    keyword_shifts = [ord(char) - ord('A') for char in keyword]

    keyword_index = 0  # This will keep track of keyword position

    for char in ciphertext:
        if char.isalpha():  # Only shift alphabetic characters
            shift = keyword_shifts[keyword_index % keyword_length]
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted_text.append(decrypted_char)
            keyword_index += 1  # Move to the next keyword letter only for alphabetic characters
        else:
            decrypted_text.append(char)  # Non-alphabetic characters remain unchanged

    return ''.join(decrypted_text)
