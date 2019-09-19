from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import random, string


class EncryptAES():
    def __init__(self):
        self.key = 'abcdegfg12345678'
        self.iv = 'abcdegfg12345678'
        self.mode = AES.MODE_CBC

    # 加密
    # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)
        length = 16
        count = len(text)
        if count % length != 0:
            add = length - (count % length)
        else:
            add = 0
        text = text + ('\0' * add)
        ciphertext = cryptor.encrypt(text)
        # 加密后的字符串转化为16进制字符串 ,当然也可以转换为base64加密的内容，可以使用b2a_base64(self.ciphertext)
        # 添加8位随机数作为扰码
        return b2a_hex(ciphertext).decode() + VariableAction.get_random_str()

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)
        # 先去除末尾的8位扰码, 需跟加密对应
        plaintext = cryptor.decrypt(a2b_hex(text[:-8]))
        return plaintext.decode().strip('\0')

        @staticmethod
        def get_random_string(length='8'):
            return ''.join(random.sample(string.ascii_letters + string.digits, length))


if __name__ == '__main__':
    aes = EncryptAES()  # 初始化密钥
    e_result = aes.encrypt("dmeo")
    d_result = pc.decrypt(e_result)
    print(en_result)
    print(d_result)