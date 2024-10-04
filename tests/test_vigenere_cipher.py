# test_vigenere.py
# This script contains unit tests for the Vigenère Cipher encryption and decryption functions.

import unittest
from encryption.vigenere_cipher import vigenere_encrypt, vigenere_decrypt

class TestVigenereCipher(unittest.TestCase):

    def test_vigenere_encrypt(self):
        # Test encryption using Vigenère Cipher with keyword "KEY"
        plaintext = "HELLO WORLD"
        keyword = "KEY"
        expected_ciphertext = "RIJVS UYVJN"
        self.assertEqual(vigenere_encrypt(plaintext, keyword), expected_ciphertext)

        # Test encryption with lowercase keyword and message
        plaintext = "attackatdawn"
        keyword = "lemon"
        expected_ciphertext = "lxfopvefrnhr"
        self.assertEqual(vigenere_encrypt(plaintext, keyword), expected_ciphertext)

    def test_vigenere_decrypt(self):
        # Test decryption using Vigenère Cipher with keyword "KEY"
        ciphertext = "RIJVS UYVJN"
        keyword = "KEY"
        expected_plaintext = "HELLO WORLD"
        self.assertEqual(vigenere_decrypt(ciphertext, keyword), expected_plaintext)

        # Test decryption with lowercase keyword and message
        ciphertext = "lxfopvefrnhr"
        keyword = "lemon"
        expected_plaintext = "attackatdawn"
        self.assertEqual(vigenere_decrypt(ciphertext, keyword), expected_plaintext)

if __name__ == '__main__':
    unittest.main()
