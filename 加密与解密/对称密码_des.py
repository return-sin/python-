# DES
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

class DESCipher:
    def __init__(self, key) -> None:
        self.block_size = DES.block_size
        self.key = key

    def encrypt(self, plaintext):
        iv = get_random_bytes(self.block_size)
        cipher = DES.new(self.key, DES.MODE_CBC, iv)
        padded_text = pad(plaintext.encode("utf-8"), self.block_size)
        encrypted_text = cipher.encrypt(padded_text)
        return base64.b64encode(iv + encrypted_text).decode("utf-8")

    def decrypt(self, ciphertext):
        decoded_text = base64.b64decode(ciphertext)
        iv = decoded_text[: self.block_size]
        cipher = DES.new(self.key, DES.MODE_CBC, iv)
        decrypted_text = unpad(
            cipher.decrypt(decoded_text[self.block_size :]), self.block_size
        )
        return decrypted_text.decode("utf-8")


def main():
    key = b"12345678"
    des_cipher = DESCipher(key)
    plaintext = "hello world"
    ciphertext = des_cipher.encrypt(plaintext)
    print("加密后的文本：", ciphertext)
    decrypted_text = des_cipher.decrypt(ciphertext)
    print("解密后的文本：", decrypted_text)


if __name__ == "__main__":
    main()
