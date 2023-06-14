import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

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

# 將密文轉換為Base64編碼的字符串
def convert_to_base64(ciphertext):
    ciphertext_bytes = base64.b64encode(ciphertext)
    ciphertext_string = ciphertext_bytes.decode('utf-8')
    return ciphertext_string

# 使用RSA加密並將密文轉換為Base64編碼的字符串
def encrypt_and_convert_to_base64(public_key, plaintext):
    # 使用公鑰進行加密
    ciphertext = encrypt_message(public_key, plaintext)
    # 將密文轉換為Base64編碼的字符串
    ciphertext_string = convert_to_base64(ciphertext)
    return ciphertext_string


