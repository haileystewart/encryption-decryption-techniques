# test_shift_cipher.py
# This script contains unit tests for the Shift Cipher (Caesar Cipher) encryption and decryption functions.

import unittest
from encryption.shift_cipher import shift_cipher_encrypt, shift_cipher_decrypt

class TestShiftCipher(unittest.TestCase):

    def test_shift_cipher_encrypt(self):
        # Test basic encryption
        self.assertEqual(shift_cipher_encrypt("Hello", 3), "Khoor")
        self.assertEqual(shift_cipher_encrypt("abc", 1), "bcd")
        self.assertEqual(shift_cipher_encrypt("xyz", 3), "abc")
        self.assertEqual(shift_cipher_encrypt("ABC", 2), "CDE")
        
        # Test encryption with non-alphabetic characters (should remain unchanged)
        self.assertEqual(shift_cipher_encrypt("Hello, World!", 3), "Khoor, Zruog!")
        self.assertEqual(shift_cipher_encrypt("123 Hello", 3), "123 Khoor")
    
    def test_shift_cipher_decrypt(self):
        # Test basic decryption
        self.assertEqual(shift_cipher_decrypt("Khoor", 3), "Hello")
        self.assertEqual(shift_cipher_decrypt("bcd", 1), "abc")
        self.assertEqual(shift_cipher_decrypt("abc", 3), "xyz")
        self.assertEqual(shift_cipher_decrypt("CDE", 2), "ABC")
        
        # Test decryption with non-alphabetic characters (should remain unchanged)
        self.assertEqual(shift_cipher_decrypt("Khoor, Zruog!", 3), "Hello, World!")
        self.assertEqual(shift_cipher_decrypt("123 Khoor", 3), "123 Hello")

if __name__ == '__main__':
    unittest.main()
