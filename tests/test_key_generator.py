# test_key_generation.py
# This script contains unit tests for the key generation and validation functions.

import unittest
from utils.key_generator import generate_aes_key, generate_des_key, generate_3des_key, validate_key

class TestKeyGeneration(unittest.TestCase):

    def test_generate_aes_key_128(self):
        # Test AES key generation for 128 bits (16 bytes)
        key = generate_aes_key(128)
        self.assertEqual(len(key), 16)
        self.assertTrue(validate_key(key, 16))

    def test_generate_aes_key_192(self):
        # Test AES key generation for 192 bits (24 bytes)
        key = generate_aes_key(192)
        self.assertEqual(len(key), 24)
        self.assertTrue(validate_key(key, 24))

    def test_generate_aes_key_256(self):
        # Test AES key generation for 256 bits (32 bytes)
        key = generate_aes_key(256)
        self.assertEqual(len(key), 32)
        self.assertTrue(validate_key(key, 32))

    def test_generate_des_key(self):
        # Test DES key generation (8 bytes)
        key = generate_des_key()
        self.assertEqual(len(key), 8)
        self.assertTrue(validate_key(key, 8))

    def test_generate_3des_key(self):
        # Test 3DES key generation (either 14 or 21 bytes)
        key = generate_3des_key()
        self.assertIn(len(key), [14, 21])
        self.assertTrue(validate_key(key, len(key)))

    def test_invalid_aes_key(self):
        # Test validation fails for an incorrect AES key size
        key = generate_aes_key(128)
        with self.assertRaises(ValueError):
            validate_key(key, 24)  # Invalid length (expecting 24 bytes, generated 16 bytes)

if __name__ == '__main__':
    unittest.main()
