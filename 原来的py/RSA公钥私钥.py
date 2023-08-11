from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# 生成RSA公钥和私钥
key = RSA.generate(2048)
public_key = key.publickey().exportKey()
private_key = key.exportKey()

# 加密数据
cipher = PKCS1_OAEP.new(key.publickey())
data = b"Hello, World!"
encrypted_data = cipher.encrypt(data)

# 解密数据
cipher = PKCS1_OAEP.new(key)
decrypted_data = cipher.decrypt(encrypted_data)

# 打印结果
print("Public key: ", public_key.decode())
print("Private key: ", private_key.decode())
print("Encrypted data: ", encrypted_data)
print("Decrypted data: ", decrypted_data.decode())