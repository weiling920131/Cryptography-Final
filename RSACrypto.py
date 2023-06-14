import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# 生成RSA金鑰對
def generate_rsa_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# 使用公鑰加密訊息
def encrypt_message(public_key, message):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

# 使用私鑰解密訊息
def decrypt_message(private_key, encrypted_message):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()

# 範例使用
# private_key, public_key = generate_rsa_key_pair()
# print("Private Key: ", private_key)
# print("Public Key: ",public_key)
# message = "Hello, World!"

# encrypted_message = encrypt_message(public_key, message)
# print("加密後的訊息:", encrypted_message)

# decrypted_message = decrypt_message(private_key, encrypted_message)
# print("解密後的訊息:", decrypted_message)
