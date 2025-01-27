# RC4
from Crypto.Cipher import ARC4

class RC4Cipher:
    def __init__(self, key) -> None:
        """初始化 RC4 算法的密钥"""
        self.key = key

    def encrypt(self, plaintext):
        """使用 RC4 算法加密数据"""
        cipher = ARC4.new(self.key)
        ciphertext = cipher.encrypt(plaintext)
        return ciphertext

    def decrypt(self, ciphertext):
        """使用 RC4 算法解密数据"""
        cipher = ARC4.new(self.key)
        plaintext = cipher.decrypt(ciphertext)
        return plaintext


def main():
    key = b"secret_key"
    plaintext = b"Hello, World!"
    cipher = RC4Cipher(key)
    ciphertext = cipher.encrypt(plaintext)
    print("Ciphertext:", ciphertext)
    plaintext = cipher.decrypt(ciphertext)
    print("Plaintext:", plaintext)


if __name__ == "__main__":
    main()
