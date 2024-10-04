# main.py
# This script runs the main menu and user input for choosing the encryption and decryption techniques.

from encryption.shift_cipher import shift_cipher_encrypt, shift_cipher_decrypt
from encryption.transposition_cipher import simple_transposition_encrypt, simple_transposition_decrypt
from encryption.vigenere_cipher import vigenere_encrypt, vigenere_decrypt
from encryption.permutation_cipher import permutation_encrypt, permutation_decrypt
from utils.key_generator import generate_aes_key, generate_des_key, generate_3des_key
from utils.padding import pad, unpad

def display_menu():
    """Display the encryption/decryption menu options."""
    print("\nSelect encryption technique:")
    print("1. Shift Cipher (Caesar Cipher)")
    print("2. Simple Transposition Cipher (Rail Fence)")
    print("3. Vigenère Cipher")
    print("4. Permutation Cipher")
    print("5. AES Encryption (Block Cipher)")
    print("6. DES Encryption (Block Cipher)")
    print("7. 3DES Encryption (Block Cipher)")
    print("8. Exit")

def handle_block_cipher_encryption(cipher_func, block_size, generate_key_func):
    # Handle encryption for block ciphers (AES, DES, 3DES)
    plaintext = input("Enter plaintext: ")
    padded_text = pad(plaintext, block_size)  # Pad the text to block size
    
    key_choice = input("Do you want to provide a key? (y/n): ")
    if key_choice.lower() == 'y':
        key = input("Enter the key (in bytes): ").encode()  # For simplicity, assume key is in bytes
    else:
        key = generate_key_func()  # Use the key generator for the selected cipher
    
    ciphertext = cipher_func(padded_text, key)  # Assuming you have a function for AES, DES encryption
    print(f"Ciphertext: {ciphertext}")
    
    decrypt = input("Do you want to decrypt this message? (y/n): ")
    if decrypt.lower() == 'y':
        decrypted_text = cipher_func(ciphertext, key, decrypt=True)  # Assuming you handle decryption with this
        unpadded_text = unpad(decrypted_text, block_size)
        print(f"Decrypted Text: {unpadded_text}")

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
            num_rows = int(input("Enter number of rows for transposition: "))
            ciphertext = simple_transposition_encrypt(plaintext, num_rows)
            print(f"Ciphertext: {ciphertext}")
            decrypt = input("Do you want to decrypt this message? (y/n): ")
            if decrypt.lower() == 'y':
                decrypted_text = simple_transposition_decrypt(ciphertext, num_rows)
                print(f"Decrypted Text: {decrypted_text}")

        elif choice == '3':
            # Vigenère Cipher
            plaintext = input("Enter plaintext: ")
            keyword = input("Enter keyword: ")
            ciphertext = vigenere_encrypt(plaintext, keyword)
            print(f"Ciphertext: {ciphertext}")
            decrypt = input("Do you want to decrypt this message? (y/n): ")
            if decrypt.lower() == 'y':
                decrypted_text = vigenere_decrypt(ciphertext, keyword)
                print(f"Decrypted Text: {decrypted_text}")

        elif choice == '4':
            # Permutation Cipher
            plaintext = input("Enter plaintext: ")
            key = input("Enter permutation key as space-separated integers: ")
            key = [int(k) for k in key.split()]
            ciphertext = permutation_encrypt(plaintext, key)
            print(f"Ciphertext: {ciphertext}")
            decrypt = input("Do you want to decrypt this message? (y/n): ")
            if decrypt.lower() == 'y':
                decrypted_text = permutation_decrypt(ciphertext, key)
                print(f"Decrypted Text: {decrypted_text}")

        elif choice == '5':
            # AES Encryption
            handle_block_cipher_encryption(aes_encrypt_function, 16, generate_aes_key)

        elif choice == '6':
            # DES Encryption
            handle_block_cipher_encryption(des_encrypt_function, 8, generate_des_key)

        elif choice == '7':
            # 3DES Encryption
            handle_block_cipher_encryption(tdes_encrypt_function, 8, generate_3des_key)

        elif choice == '8':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
