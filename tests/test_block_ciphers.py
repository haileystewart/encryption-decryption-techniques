# test_block_ciphers.py
# This script contains unit tests for the Block Cipher encryption and decryption functions.

import unittest
from encryption.block_ciphers import aes_encrypt, aes_decrypt, des_encrypt, des_decrypt, generate_aes_key, generate_des_key, generate_iv

class TestBlockCiphers(unittest.TestCase):

    def test_aes_ecb_encrypt_decrypt(self):
        plaintext = "This is a secret message."
        key = generate_aes_key(16)  # 128-bit key
        ciphertext = aes_encrypt(plaintext, key, mode='ECB')
        decrypted_text = aes_decrypt(ciphertext, key, mode='ECB')
        self.assertEqual(plaintext, decrypted_text)

    def test_aes_cbc_encrypt_decrypt(self):
        plaintext = "This is a secret message."
        key = generate_aes_key(16)  # 128-bit key
        iv = generate_iv(16)  # 16-byte IV for AES
        ciphertext = aes_encrypt(plaintext, key, mode='CBC', iv=iv)
        decrypted_text = aes_decrypt(ciphertext, key, mode='CBC', iv=iv)
        self.assertEqual(plaintext, decrypted_text)

    def test_des_ecb_encrypt_decrypt(self):
        plaintext = "SecretMsg"
        key = generate_des_key()  # 8-byte key
        ciphertext = des_encrypt(plaintext, key, mode='ECB')
        decrypted_text = des_decrypt(ciphertext, key, mode='ECB')
        self.assertEqual(plaintext, decrypted_text)

    def test_des_cbc_encrypt_decrypt(self):
        plaintext = "SecretMsg"
        key = generate_des_key()  # 8-byte key
        iv = generate_iv(8)  # 8-byte IV for DES
        ciphertext = des_encrypt(plaintext, key, mode='CBC', iv=iv)
        decrypted_text = des_decrypt(ciphertext, key, mode='CBC', iv=iv)
        self.assertEqual(plaintext, decrypted_text)

if __name__ == '__main__':
    unittest.main()
