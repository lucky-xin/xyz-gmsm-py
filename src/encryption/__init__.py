__title__ = 'serialization'
__author__ = 'chaoxin.lu'
__email__ = 'chaoxin.lu@pistonint.com'

__all__ = ['SM2Encryption']

import base64
import json

from gmssl import sm2


class SM2Encryption(object):
    def __init__(self, private_key: str, public_key: str):
        self._public_key = public_key
        self._private_key = private_key

    def encrypt(self, plain_byts: bytes, asn1: bool = True, mode: int = 1) -> bytes:
        """
        使用SM2算法加密给定的字节数据。

        SM2是一种基于椭圆曲线密码学的公钥加密算法，广泛用于中国国内的加密应用。
        该函数通过CryptSM2类实例化一个SM2对象来进行加密操作，支持ASN.1编码和不同的操作模式。

        参数:
        - plain_byts: 待加密的原始字节数据。
        - asn1: 是否使用ASN.1编码，默认为True。ASN.1编码是SM2加密的一种标准格式。
        - mode: 加密模式，默认为1。不同的模式可能适用于不同的安全需求或性能需求。

        返回:
        加密后的字节数据。

        注意:
        - 该函数使用了预置的公钥和私钥，这意味着它要么用于签名验证（使用公钥），要么用于加密（使用私钥）。
        - 实际应用中，公钥和私钥的使用应根据具体的加密通信场景和安全需求进行严格管理。
        """
        # 实例化SM2加密对象，准备进行加密操作
        sm2_crypt = sm2.CryptSM2(
            public_key=self._public_key,
            private_key=self._private_key,
            asn1=asn1,
            mode=mode)

        # 执行加密并返回加密后的数据
        return sm2_crypt.encrypt(plain_byts)

    def encrypt_2_hex(self, plain_byts: bytes, asn1: bool = True, mode: int = 1) -> str:
        """
        加密给定的字节数据，并以十六进制字符串形式返回加密结果。

        该方法首先调用 `encrypt` 方法对输入的明文字节进行加密，然后将加密结果转换为十六进制字符串格式。
        这种格式化后的输出常用于需要文本表示的场景，例如日志记录或用户界面显示。

        参数:
        - plain_byts: 待加密的字节数据。
        - asn1: 是否使用ASN.1编码的布尔值。ASN.1编码可以更有效地表示某些数据结构。
        - mode: 加密模式的整数值，用于指定加密算法的具体模式或配置。

        返回值:
        - 返回加密后的数据的十六进制字符串表示。

        注意:
        - 该方法依赖于内部 `encrypt` 方法进行实际的加密操作。
        - 转换为十六进制字符串是为了便于传输或存储，同时避免了二进制数据在处理过程中的潜在问题。
        """
        # 调用encrypt方法进行加密，然后将结果转为十六进制字符串
        return self.encrypt(plain_byts, asn1, mode).hex()

    def encrypt_2_base64(self, plain_text, asn1: bool = True, mode: int = 1) -> str:
        """
        使用Base64编码加密明文。

        该方法首先使用self.encrypt方法加密明文，然后将加密结果使用Base64编码，
        最后返回Base64编码后的字符串。这种方法常用于需要通过不安全的信道
        传输数据时，增加数据的安全性。

        参数:
        plain_text: 待加密的明文字符串。
        asn1 (bool): 指定是否使用ASN.1编码，默认为True。
        mode (int): 指定加密模式，默认为1。

        返回:
        str: Base64编码后的加密字符串。
        """
        # 调用encrypt方法加密明文，并使用Base64编码
        return base64.b64encode(self.encrypt(plain_text, asn1, mode)).decode('utf8')

    def decrypt(self, cipher_byts: bytes, asn1: bool = True, mode: int = 1) -> bytes:
        """
        使用SM2算法解密给定的密文。

        :param cipher_byts: 待解密的密文，以字节形式表示。
        :param asn1: 是否使用ASN.1编码格式。默认为True。
        :param mode: SM2加密模式。默认为1，表示基本加密模式。
        :return: 解密后的明文，以字节形式返回。

        本函数通过CryptSM2类创建一个SM2加密对象，然后使用该对象的decrypt方法
        来解密传入的密文。函数接收公钥和私钥，以及是否使用ASN.1编码格式和加密模式，
        并返回解密后的明文数据。
        """
        # 创建SM2加密对象，初始化时指定公钥、私钥、ASN.1编码格式以及加密模式
        sm2_crypt = sm2.CryptSM2(
            public_key=self._public_key,
            private_key=self._private_key,
            asn1=asn1,
            mode=mode)

        # 使用SM2加密对象的解密方法解密密文，返回解密后的明文数据
        return sm2_crypt.decrypt(cipher_byts)

    def decrypt_base64(self, cipher_text: str, asn1: bool = True, mode: int = 1) -> bytes:
        """
        使用Base64解密给定的密文。

        :param cipher_text: 需要解密的Base64格式的密文。
        :param asn1: 是否使用ASN.1编码，默认为True。
        :param mode: 解密模式，默认为1。
        :return: 解密后的字节数据。
        """
        # 移除密文前的特定前缀，如果存在的话
        cipher_text = cipher_text.lstrip("MDQ=") if cipher_text.startswith("MDQ=") else cipher_text
        # 调用底层的decrypt方法进行实际解密操作，传入Base64解码后的密文
        return self.decrypt(base64.b64decode(cipher_text), asn1, mode)

    def decrypt_hex(self, cipher_text: str, asn1: bool = True, mode: int = 1) -> bytes:
        """
        解密给定的十六进制密文。

        :param cipher_text: 待解密的十六进制密文。
        :param asn1: 是否使用ASN.1编码，默认为True。
        :param mode: 解密模式，默认为1。
        :return: 解密后的字节数据。
        """
        # 如果密文以“04”开头，则去掉前导“04”；否则，密文保持不变。
        cipher_text = cipher_text.lstrip("04") if cipher_text.startswith("04") else cipher_text
        # 将十六进制密文转换为字节，并调用decrypt方法进行解密。
        return self.decrypt(bytes.fromhex(cipher_text), asn1, mode)

    def decrypt_object(self, cipher_byts: bytes, asn1: bool = True, mode: int = 1) -> dict:
        """
        解密给定的密文字节，返回一个字典对象。

        此方法首先调用自身的`decrypt`方法对密文进行解密，然后将解密后的字节串
        转换为字典。如果原始数据是ASN.1编码且需要特定模式解密，可以通过参数进行指定。

        :param cipher_byts: 密文字节
        :param asn1: 布尔值，指示是否使用ASN.1编码，默认为True
        :param mode: 整数值，指定解密模式，默认为1
        :return: 解密后转换得到的字典对象
        """
        # 调用decrypt方法解密密文，得到字节串
        byts = self.decrypt(cipher_byts, asn1, mode)
        # 将解密后的字节串转换为字典并返回
        return json.loads(byts)

