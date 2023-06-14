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
    # print(encrypted_message[2:len(encrypted_message)-1], '++++++++++++++++++++++++++++++++++++++')
    decrypted_message = cipher.decrypt(encrypted_message)#[2:len(encrypted_message)-1])
    return decrypted_message.decode()

if __name__ == '__main__':
    private, public = generate_rsa_key_pair()
    print(type(private), private)
    print(type(public), public)
    message = 'fffffff'
    print(type(encrypt_message(public, message)), encrypt_message(public, message))
    print(type(decrypt_message(private, encrypt_message(public, message))), decrypt_message(private, encrypt_message(public, message)))

