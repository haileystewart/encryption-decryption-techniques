# test_transposition_cipher.py
# This script contains unit tests for the Columnar Transposition Cipher encryption and decryption functions.

import unittest
from encryption.transposition_cipher import transposition_encrypt, transposition_decrypt, double_transposition_encrypt, double_transposition_decrypt

class TestTranspositionCipher(unittest.TestCase):

    def test_simple_transposition_encrypt(self):
        # Simple transposition encryption test
        self.assertEqual(transposition_encrypt("HELLO WORLD", "321"), "HOLEWDLOLR")

    def test_simple_transposition_decrypt(self):
        # Simple transposition decryption test
        self.assertEqual(transposition_decrypt("HOLEWDLOLR", "321"), "HELLOWORLD")

    def test_double_transposition_encrypt(self):
        # Double transposition encryption test
        self.assertEqual(double_transposition_encrypt("HELLO WORLD", "321", "4321"), "HLLORDEOOW")

    def test_double_transposition_decrypt(self):
        # Double transposition decryption test
        self.assertEqual(double_transposition_decrypt("HLLORDEOOW", "321", "4321"), "HELLOWORLD")

    def test_empty_string(self):
        # Test empty string encryption and decryption
        self.assertEqual(transposition_encrypt("", "321"), "")
        self.assertEqual(transposition_decrypt("", "321"), "")
        self.assertEqual(double_transposition_encrypt("", "321", "4321"), "")
        self.assertEqual(double_transposition_decrypt("", "321", "4321"), "")

    def test_single_character(self):
        # Test single character encryption and decryption
        self.assertEqual(transposition_encrypt("A", "321"), "A")
        self.assertEqual(transposition_decrypt("A", "321"), "A")
        self.assertEqual(double_transposition_encrypt("A", "321", "4321"), "A")
        self.assertEqual(double_transposition_decrypt("A", "321", "4321"), "A")

    def test_key_larger_than_message(self):
        # Test when the key is larger than the message length
        self.assertEqual(transposition_encrypt("SHORT", "321"), "SOTHR")
        self.assertEqual(transposition_decrypt("SOTHR", "321"), "SHORT")
        self.assertEqual(double_transposition_encrypt("SHORT", "321", "4321"), "SOTHR")
        self.assertEqual(double_transposition_decrypt("SOTHR", "321", "4321"), "SHORT")

if __name__ == '__main__':
    unittest.main()
