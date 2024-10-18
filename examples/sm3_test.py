from src.encryption import SM3

if __name__ == '__main__':
    data = "04b89e21ff8434dc55f0f60563c86a976234bf6fc2ccb2d4b7fb9948b52dc5319efd2619faf5c289c2ea638cf33523b3fbf9df41dd115f1edec5d9a9f922d754e1bc30e3368265d4728bf3e0d5473d2d96b0d9e498e5cbcaaef179f45bd52e50af0155ef410651f47b238593817eb8ed";
    hash = "5377795931ae4eab35c70c3e4ef8b0b76a5793b4b50e5c1bde672eae7fdb23a5"

    sm3 = SM3()
    encode = sm3.hash(data)
    print(encode)
    print(encode==hash)