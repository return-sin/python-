# RSA
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

class RSACipher:
    def __init__(self, key_size=2048) -> None:
        self.key_size = key_size
        self.private_key = None
        self.public_key = None

    def generate_key(self):
        key = RSA.generate(self.key_size)
        self.private_key = key.export_key()
        self.public_key = key.publickey().export_key()
        return self.private_key, self.public_key

    def encrypt(self, plaintext):
        self.generate_key()
        rsa_public_key = RSA.import_key(self.public_key) # type: ignore
        cipher = PKCS1_OAEP.new(rsa_public_key)
        encrypted_message = cipher.encrypt(plaintext.encode("utf-8"))
        return binascii.hexlify(encrypted_message).decode("utf-8")

    def decrypt(self, encrypted_message):
        rsa_private_key = RSA.import_key(self.private_key)# type: ignore
        cipher = PKCS1_OAEP.new(rsa_private_key)
        decrypted_message = cipher.decrypt(binascii.unhexlify(encrypted_message))
        return decrypted_message.decode("utf-8")


def main():
    rsa_cipher = RSACipher()
    plaintext = "Hello, World!"
    encrypted_message = rsa_cipher.encrypt(plaintext)
    print(f"Encrypted message: {encrypted_message}")
    decrypted_message = rsa_cipher.decrypt(encrypted_message)
    print(f"Decrypted message: {decrypted_message}")


if __name__ == "__main__":
    main()
