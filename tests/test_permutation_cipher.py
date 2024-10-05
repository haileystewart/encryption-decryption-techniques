# test_permutation_cipher.py
# This script contains unit tests for the updated Permutation Cipher encryption and decryption functions.

import unittest
import random
from encryption.permutation_cipher import encrypt, decrypt, generate_valid_block_size, generate_permutation_key

class TestPermutationCipher(unittest.TestCase):

    def test_generate_valid_block_size(self):
        # Test that the generated block size is a factor of the message length
        random.seed(1)
        message_length = 15
        valid_block_size = generate_valid_block_size(message_length)
        self.assertIn(valid_block_size, [3, 5, 15])

    def test_generate_permutation_key(self):
        # Test the generation of a random permutation key
        random.seed(0)
        self.assertEqual(generate_permutation_key(4), [2, 0, 1, 3])

    def test_permutation_encrypt(self):
        # Test encryption with a provided key
        message = "HELLO WORLD"
        key = [2, 0, 1]
        encrypted_message, _ = encrypt(message, key=key, block_size=3)
        expected_encrypted_message = "EHLLOWLORD"
        self.assertEqual(encrypted_message, expected_encrypted_message)

    def test_permutation_decrypt(self):
        # Test decryption with a provided key
        encrypted_message = "EHLLOWLORD"
        key = [2, 0, 1]
        expected_plaintext = "HELLOWORLD"
        decrypted_message = decrypt(encrypted_message, key)
        self.assertEqual(decrypted_message, expected_plaintext)

if __name__ == '__main__':
    unittest.main()
