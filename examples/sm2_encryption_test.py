from src.encryption import SM2Encryption

if __name__ == '__main__':
    private_key = '90bb8703d31503624a526f766cfa47d3d8c10055e94046bf99b56cecc9aa4bb6'
    public_key = '04ca5bf8843863d518bfbed316c6b67c7f807fc3436790556c336ddf3a1ca93ae7537f658c222c7f307be57328222256e12d2e26abb8e0160d2501306d64b41266'

    encryption = SM2Encryption(private_key, public_key)
    plaintext = "你可以根据具体需求正确地挂载文件或目录到Kubernetes Pod内的容器中。如果有任何其他问题或需要进一步的帮助，请随时提问。"

    enc_data = encryption.encrypt_2_hex(plaintext.encode(), True, 1)
    print(enc_data)
    print('------------------')

    dec_data1 = encryption.decrypt_hex(enc_data, True, 1)
    print(dec_data1.decode())
    print('------------------')

    enc_data = encryption.encrypt_2_base64(plaintext.encode(), True, 1)
    print(enc_data)
    print('------------------')

    dec_data1 = encryption.decrypt_base64(enc_data, True, 1)
    print(dec_data1.decode())
    print('------------------')
