# AES
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

class AESCipher:
    def __init__(self, key) -> None:
        self.key = key
        self.block_size = AES.block_size

    def encrypt(self, plaintext):
        iv = get_random_bytes(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(plaintext.encode("utf-8"), self.block_size))
        return base64.b64encode(iv + ciphertext).decode("utf-8")

    def decrypt(self, ciphertext):
        ciphertext = base64.b64decode(ciphertext)
        iv = ciphertext[: self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plaintext = unpad(
            cipher.decrypt(ciphertext[self.block_size :]), self.block_size
        )
        return plaintext.decode("utf-8")


def main():
    key = b"0123456789abcdef"
    aes_cipher = AESCipher(key)
    plaintext = "Hello,world!"
    encrypted_text = aes_cipher.encrypt(plaintext)
    print("加密后的文本：", encrypted_text)
    decrypted_text = aes_cipher.decrypt(encrypted_text)
    print("解密后的文本：", decrypted_text)


if __name__ == "__main__":
    main()
