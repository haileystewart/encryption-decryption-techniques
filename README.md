Encryption-Decryption-Techniques
Objective
This project is a command-line program that implements multiple encryption and decryption techniques. The techniques covered in this project include substitution ciphers, transposition ciphers, and advanced encryption algorithms. The goal is to provide a simple yet comprehensive tool to explore different encryption methods while ensuring that the user can encrypt and decrypt messages using a variety of options.

Program Features
The program supports the following features:

Encryption Techniques:
Substitution Ciphers:

Shift Cipher (Caesar Cipher): A simple cipher that shifts characters by a specified number of positions.
Permutation Cipher: A cipher that permutes the characters of the plaintext based on a predefined pattern.
Transposition Ciphers:

Simple Transposition Cipher: Rearranges characters of the plaintext in a simple pattern (e.g., Rail Fence Cipher).
Double Transposition Cipher: Applies two layers of transposition to the plaintext for enhanced security.
Vigenère Cipher: A polyalphabetic substitution cipher that uses a keyword to determine the shifts in the plaintext.

Advanced Encryption Algorithms:

AES-128 (Advanced Encryption Standard)
DES (Data Encryption Standard)
3DES (Triple DES)
Encryption Modes:
ECB (Electronic Codebook)
CBC (Cipher Block Chaining)
CFB (Cipher Feedback)
OFB (Output Feedback)
Program Flow:
The program displays a list of available encryption techniques.
The user selects an encryption technique and enters the plaintext to be encrypted.
For encryption algorithms like AES, DES, or 3DES, the size of the message must be greater than the block size of the algorithm.
The user can choose to provide an encryption key or use a default key.
The program encrypts the message and displays the encrypted result (ciphertext).
The user can also choose the decryption option, where the ciphertext and decryption key are used to retrieve the original plaintext.
Decryption:
When the user selects decryption, they provide the ciphertext and the decryption technique. The program either uses the same key as encryption (default) or accepts a user-provided key.