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
    # print(encrypted_message[2:len(encrypted_message)-1], '++++++++++++++++++++++++++++++++++++++')
    decrypted_message = cipher.decrypt(encrypted_message)#[2:len(encrypted_message)-1])
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



if __name__ == '__main__':
    private, public = generate_rsa_key_pair()
    # print(type(private), private)
    # print(type(public), public)
    # print(bytes(str(private)[2:len(str(private))-1],'utf-8'))
    # print(public.decode())
    message = 'fffffff'
    one = encrypt_message(public, message)
    print(one)
    test = str(one)[2:len(str(one))-1].split('\\')
    cipher = ''
    for word in test:
        cipher+=word
    print(cipher)
    # print(bytes(,'utf-8'))
    print('\n')
    # print(bytes(one[2:len(one)-1],'utf-8'))
    # print(decrypt_message(private, bytes(one[2:len(one)-1],'utf-8')))
    # print('\n')
    # print(str(encrypt_message(public, message))[:])
    # print(type(decrypt_message(private, encrypt_message(public, message))), decrypt_message(private, encrypt_message(public, message)))

    # 範例使用
    public_key = "這裡放入您的RSA公鑰"  # 請替換為實際的RSA公鑰
    plaintext = "Hello, World!"

    ciphertext_string = encrypt_and_convert_to_base64(public, plaintext)
    print("Base64編碼的密文:", type(ciphertext_string))
    print("Base64解碼:", base64.b64decode(ciphertext_string))
    print("明文:", decrypt_message(private,base64.b64decode(ciphertext_string)))
    print('++++++++++\n+++++++++++\n')
    m = private
    print(m)
    print(convert_to_base64(m))
    print(base64.b64decode(convert_to_base64(m)))

