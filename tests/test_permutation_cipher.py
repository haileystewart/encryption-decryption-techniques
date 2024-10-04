# test_permutation_cipher.py
# This script contains unit tests for the Permutation Cipher encryption and decryption functions.

import unittest
from encryption.permutation_cipher import permutation_encrypt, permutation_decrypt

class TestPermutationCipher(unittest.TestCase):

    def test_permutation_encrypt(self):
        # Test encryption with key [3, 1, 2]
        plaintext = "HELLO WORLD"
        key = [3, 1, 2]
        expected_ciphertext = "LEH LOOLWRD"
        self.assertEqual(permutation_encrypt(plaintext, key), expected_ciphertext)

        # Test encryption with key [4, 3, 1, 2]
        plaintext = "PERMUTATION CIPHER"
        key = [4, 3, 1, 2]
        expected_ciphertext = "MUPETIORCNPHIATREA"
        self.assertEqual(permutation_encrypt(plaintext, key), expected_ciphertext)

    def test_permutation_decrypt(self):
        # Test decryption with key [3, 1, 2]
        ciphertext = "LEH LOOLWRD"
        key = [3, 1, 2]
        expected_plaintext = "HELLO WORLD"
        self.assertEqual(permutation_decrypt(ciphertext, key), expected_plaintext)

        # Test decryption with key [4, 3, 1, 2]
        ciphertext = "MUPETIORCNPHIATREA"
        key = [4, 3, 1, 2]
        expected_plaintext = "PERMUTATION CIPHER"
        self.assertEqual(permutation_decrypt(ciphertext, key), expected_plaintext)

if __name__ == '__main__':
    unittest.main()
