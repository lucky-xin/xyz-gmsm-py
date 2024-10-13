from src.encryption import SM2Encryption

private_key = '90bb8703d31503624a526f766cfa47d3d8c10055e94046bf99b56cecc9aa4bb6'
public_key = '04ca5bf8843863d518bfbed316c6b67c7f807fc3436790556c336ddf3a1ca93ae7537f658c222c7f307be57328222256e12d2e26abb8e0160d2501306d64b41266'
encryption = SM2Encryption(private_key, public_key)

plaintext = "国密算法SM2".encode()
enc_data = encryption.encrypt(plaintext, True, 1)

print(enc_data.hex())
print('------------------')

dec_data1 = encryption.decrypt(enc_data.hex(), True, 1)

print(dec_data1.decode())
print('------------------')

enc_data = '04b89e21ff8434dc55f0f60563c86a976234bf6fc2ccb2d4b7fb9948b52dc5319efd2619faf5c289c2ea638cf33523b3fbf9df41dd115f1edec5d9a9f922d754e1bc30e3368265d4728bf3e0d5473d2d96b0d9e498e5cbcaaef179f45bd52e50af0155ef410651f47b238593817eb8ed'
dec_data2 = encryption.decrypt(enc_data, True, 1)
print(dec_data2.decode() )
print(plaintext == dec_data2)


from gmssl import sm2

private_key = '90bb8703d31503624a526f766cfa47d3d8c10055e94046bf99b56cecc9aa4bb6'
public_key = '04ca5bf8843863d518bfbed316c6b67c7f807fc3436790556c336ddf3a1ca93ae7537f658c222c7f307be57328222256e12d2e26abb8e0160d2501306d64b41266'
sm2_crypt = sm2.CryptSM2(
    public_key=public_key,
    private_key=private_key,
    asn1=True,
    mode=1)
plaintext = "国密算法SM2".encode()
enc_data = sm2_crypt.encrypt(plaintext)
print(enc_data.hex())
print('------------------')
cipher_text = '04b89e21ff8434dc55f0f60563c86a976234bf6fc2ccb2d4b7fb9948b52dc5319efd2619faf5c289c2ea638cf33523b3fbf9df41dd115f1edec5d9a9f922d754e1bc30e3368265d4728bf3e0d5473d2d96b0d9e498e5cbcaaef179f45bd52e50af0155ef410651f47b238593817eb8ed'
text = cipher_text.lstrip("04") if cipher_text.startswith("04") else cipher_text
dec_data2 = sm2_crypt.decrypt(bytes.fromhex(text))
print(dec_data2.decode() )
print(plaintext == dec_data2)
