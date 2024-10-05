# main.py
# This script runs the main menu and user input for choosing the encryption and decryption techniques.

from encryption.shift_cipher import shift_cipher_encrypt, shift_cipher_decrypt
from encryption.vigenere_cipher import vigenere_encrypt, vigenere_decrypt
from encryption.permutation_cipher import encrypt as permutation_encrypt, decrypt as permutation_decrypt
from encryption.block_ciphers import aes_encrypt, aes_decrypt, des_encrypt, des_decrypt, generate_aes_key, generate_des_key, generate_iv
from utils.padding import pad, unpad
from encryption.transposition_cipher import (
    transposition_encrypt,
    transposition_decrypt,
    double_transposition_encrypt,
    double_transposition_decrypt,
)

def display_menu():
    """Display the encryption/decryption menu options."""
    print("\nSelect encryption technique:")
    print("1. Shift Cipher (Caesar Cipher)")
    print("2. Simple Transposition Cipher")
    print("3. Double Transposition Cipher")
    print("4. Vigenère Cipher")
    print("5. Permutation Cipher")
    print("6. AES Encryption (Block Cipher)")
    print("7. DES Encryption (Block Cipher)")
    print("8. Exit")

def select_mode():
    """Display the block cipher modes and return the selected mode."""
    print("Select encryption mode:")
    print("1. ECB (Electronic Codebook)")
    print("2. CBC (Cipher Block Chaining)")
    print("3. CFB (Cipher Feedback)")
    print("4. OFB (Output Feedback)")
    mode_choice = input("Enter choice (1/2/3/4): ")

    if mode_choice == '1':
        return 'ECB'
    elif mode_choice == '2':
        return 'CBC'
    elif mode_choice == '3':
        return 'CFB'
    elif mode_choice == '4':
        return 'OFB'
    else:
        print("Invalid choice, defaulting to ECB.")
        return 'ECB'

def handle_block_cipher_encryption(cipher_encrypt_func, cipher_decrypt_func, block_size, generate_key_func):
    """Handle encryption for block ciphers (AES, DES)."""
    plaintext = input("Enter plaintext (must be greater than the block size): ")
    if len(plaintext) < block_size:
        print(f"Error: Message must be longer than {block_size} characters for block cipher encryption.")
        return
    
    padded_text = pad(plaintext.encode(), block_size)  # Pad the text to block size
    
    key_choice = input("Do you want to provide a key? (y/n): ")
    if key_choice.lower() == 'y':
        key = input("Enter the key (in hex format): ")
        key = bytes.fromhex(key)  # Convert hex to bytes
    else:
        if cipher_encrypt_func == aes_encrypt:
            key_size = int(input("Enter AES key size (128/192/256): "))
            key = generate_key_func(key_size)
        else:
            key = generate_key_func()  # Use the key generator for DES

    mode = select_mode()

    # Use IV for modes other than ECB
    iv = None
    if mode in ['CBC', 'CFB', 'OFB']:
        iv = generate_iv(block_size)

    ciphertext, iv = cipher_encrypt_func(padded_text, key, mode, iv)
    print(f"Ciphertext (hex): {ciphertext.hex()}")
    if iv:
        print(f"IV (hex): {iv.hex()}")

    decrypt = input("Do you want to decrypt this message? (y/n): ")
    if decrypt.lower() == 'y':
        decrypted_bytes = cipher_decrypt_func(ciphertext, key, mode, iv)  # Ensure decryption returns bytes
        
        # Debugging step to check the decrypted data format
        print(f"Decrypted bytes (before unpadding): {decrypted_bytes}")
        try:
            unpadded_text = unpad(decrypted_bytes, block_size)  # Ensure you're unpadding bytes
            print(f"Decrypted Text: {unpadded_text.decode('utf-8')}")  # Decode to string after unpadding
        except ValueError as e:
            print(f"Error during unpadding: {e}")


def main():
    while True:
        display_menu()
        choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

        if choice == '1':
            # Shift Cipher (Caesar Cipher)
            plaintext = input("Enter plaintext: ")
            key = int(input("Enter shift key: "))
            ciphertext = shift_cipher_encrypt(plaintext, key)
            print(f"Ciphertext: {ciphertext}")
            decrypt = input("Do you want to decrypt this message? (y/n): ")
            if decrypt.lower() == 'y':
                decrypted_text = shift_cipher_decrypt(ciphertext, key)
                print(f"Decrypted Text: {decrypted_text}")

        elif choice == '2':
            # Simple Transposition Cipher
            plaintext = input("Enter plaintext: ")
            key = input("Enter key for transposition: ")
            ciphertext = transposition_encrypt(plaintext, provided_key=key)
            cleaned_ciphertext = ciphertext.replace('_', '')  # Clean up padding characters
            print(f"Ciphertext: {cleaned_ciphertext}")
            decrypt = input("Do you want to decrypt this message? (y/n): ")
            if decrypt.lower() == 'y':
                decrypted_text = transposition_decrypt(ciphertext, provided_key=key)
                cleaned_decrypted_text = decrypted_text.replace('_', '')  # Clean up padding characters
                print(f"Decrypted Text: {cleaned_decrypted_text}")

        elif choice == '3':
            # Double Transposition Cipher
            plaintext = input("Enter plaintext: ")
            key1 = input("Enter the first key: ")
            key2 = input("Enter the second key: ")
            ciphertext = double_transposition_encrypt(plaintext, key1, key2)
            cleaned_ciphertext = ciphertext.replace('_', '')  # Clean up padding characters
            print(f"Ciphertext: {cleaned_ciphertext}")
            decrypt = input("Do you want to decrypt this message? (y/n): ")
            if decrypt.lower() == 'y':
                decrypted_text = double_transposition_decrypt(ciphertext, key1, key2)
                cleaned_decrypted_text = decrypted_text.replace('_', '')  # Clean up padding characters
                print(f"Decrypted Text: {cleaned_decrypted_text}")

        elif choice == '4':
            # Vigenère Cipher
            plaintext = input("Enter plaintext: ")
            keyword = input("Enter keyword: ")
            ciphertext = vigenere_encrypt(plaintext, keyword)
            print(f"Ciphertext: {ciphertext}")
            decrypt = input("Do you want to decrypt this message? (y/n): ")
            if decrypt.lower() == 'y':
                decrypted_text = vigenere_decrypt(ciphertext, keyword)
                print(f"Decrypted Text: {decrypted_text}")

        elif choice == '5':
            # Permutation Cipher
            plaintext = input("Enter plaintext: ")
            key = input("Enter permutation key as space-separated integers: ")
            key = [int(k) for k in key.split()]
            ciphertext, _ = permutation_encrypt(plaintext, key=key, block_size=len(key))
            cleaned_ciphertext = ciphertext.replace('_', '')  # Clean up padding characters
            print(f"Ciphertext: {cleaned_ciphertext}")
            decrypt = input("Do you want to decrypt this message? (y/n): ")
            if decrypt.lower() == 'y':
                decrypted_text = permutation_decrypt(ciphertext, key)
                cleaned_decrypted_text = decrypted_text.replace('_', '')  # Clean up padding characters
                print(f"Decrypted Text: {cleaned_decrypted_text}")

        elif choice == '6':
            # AES Encryption
            handle_block_cipher_encryption(aes_encrypt, aes_decrypt, 16, generate_aes_key)

        elif choice == '7':
            # DES Encryption
            handle_block_cipher_encryption(des_encrypt, des_decrypt, 8, generate_des_key)

        elif choice == '8':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
