from src.encryption import SM4

if __name__ == '__main__':
    text = "国密算法SM4"
    key = "639e29c43d62713678897f3fd26b2e87"
    iv = "84eacb3e5a3c342c81efd57da905a948"
    sm4 = SM4(bytes.fromhex(key), bytes.fromhex(iv))


    encrypt_text = sm4.encrypt_2_hex(text.encode("utf-8"))
    print(encrypt_text)
    decrypt = sm4.decrypt_hex(encrypt_text)
    print(decrypt.decode("utf-8"))

    encrypt_text = sm4.encrypt_2_base64(text.encode("utf-8"))
    print(encrypt_text)
    decrypt = sm4.decrypt_base64(encrypt_text)
    print(decrypt.decode("utf-8"))

    cipher_text = "78b8ce5510f901d77bdf802c28b52d4dfbcaf9bdc2d4cff05ff691d7ea8776151d885592858386655b5ea32450c54d496dd59a92b9fc999c6b25253e26d252ac435178a002b8ea0f060ed20e066539ec"
    decrypt = sm4.decrypt_hex(cipher_text)

    print("decrypted:", decrypt.decode("utf-8"))
