import json

from gmssl import sm2


class SM2Encryption(object):
    def __init__(self, private_key: str, public_key: str):
        self._public_key = public_key
        self._private_key = private_key

    def encrypt(self, plain_text, asn1: bool = True, mode: int = 1) -> bytes:
        sm2_crypt = sm2.CryptSM2(
            public_key=self._public_key,
            private_key=self._private_key,
            asn1=asn1,
            mode=mode)
        return sm2_crypt.encrypt(plain_text)

    def decrypt(self, cipher_text: str, asn1: bool = True, mode: int = 1) -> bytes:
        text = cipher_text.lstrip("04") if cipher_text.startswith("04") else cipher_text
        sm2_crypt = sm2.CryptSM2(
            public_key=self._public_key,
            private_key=self._private_key,
            asn1=asn1,
            mode=mode)
        return sm2_crypt.decrypt(bytes.fromhex(text))

    def decrypt_object(self, cipher_text: str, asn1: bool = True, mode: int = 1) -> dict:
        byts = self.decrypt(cipher_text, asn1, mode)
        return json.loads(byts)
