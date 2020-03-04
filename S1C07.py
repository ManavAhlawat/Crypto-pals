from base64 import b64decode
from Crypto.Cipher import AES


def aes_ecb_decrypt(data, key):
    
    cipher = AES.new(key, AES.MODE_ECB)
    return pkcs7_unpad(cipher.decrypt(data))


def main():
    with open("S1C07_input.txt") as input_file:
        binary_data = b64decode(input_file.read())
    print(aes_ecb_decrypt(binary_data, b'YELLOW SUBMARINE').decode().rstrip())


if __name__ == "__main__":
    main()