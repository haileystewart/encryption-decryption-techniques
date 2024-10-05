# test_transposition_cipher.py
# This script contains unit tests for the Columnar Transposition Cipher encryption and decryption functions.

import unittest
from encryption.transposition_cipher import transposition_encrypt, transposition_decrypt, double_transposition_encrypt, double_transposition_decrypt

class TestTranspositionCipher(unittest.TestCase):

    def test_transposition_encrypt(self):
        # Test basic transposition encryption with single key
        plaintext = "HELLO"
        key = "312"
        expected_ciphertext = "LHELO"
        result = transposition_encrypt(plaintext, key)
        self.assertEqual(result, expected_ciphertext)

    def test_transposition_decrypt(self):
        # Test basic transposition decryption with single key
        ciphertext = "LHELO"
        key = "312"
        expected_plaintext = "HELLO"
        result = transposition_decrypt(ciphertext, key)
        self.assertEqual(result, expected_plaintext)

    def test_double_transposition_encrypt(self):
        # Test double transposition encryption
        plaintext = "HELLO"
        key1 = "312"
        key2 = "431"
        expected_ciphertext = "ELHLO"  # You can adjust this as needed to match the logic
        result = double_transposition_encrypt(plaintext, key1, key2)
        self.assertEqual(result, expected_ciphertext)

    def test_double_transposition_decrypt(self):
        # Test double transposition decryption
        ciphertext = "ELHLO"  # You can adjust this based on your encryption test result
        key1 = "312"
        key2 = "431"
        expected_plaintext = "HELLO"
        result = double_transposition_decrypt(ciphertext, key1, key2)
        self.assertEqual(result, expected_plaintext)

if __name__ == "__main__":
    unittest.main()
