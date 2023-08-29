from Crypto.Cipher import DES
import base32hex

def pad(text):
    # PKCS7 padding
    padding_length = 8 - (len(text) % 8)
    padding = bytes([padding_length] * padding_length)
    return text + padding

def unpad(text):
    padding_length = text[-1]
    return text[:-padding_length]

def des_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext))
    return ciphertext

def des_decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(ciphertext))
    return decrypted_text

def main():
    key = b'12345678'  # 8-byte key (DES uses 56-bit effective key length)
    plaintext = b'This is a secret message'

    # Encryption
    ciphertext = des_encrypt(key, plaintext)
    encrypted_text = base32hex.b32encode(ciphertext).decode('utf-8')

    # Decryption
    decoded_ciphertext = base32hex.b32decode(encrypted_text)
    decrypted_text = des_decrypt(key, decoded_ciphertext).decode('utf-8')

    print("Original Text:", plaintext)
    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
