import base64
from Crypto.Cipher import AES
from src.set2.problem9.problem2_9 import pad



def main():
    print("Key:")
    key=raw_input().decode('utf-8')
    print("Input file:")
    with open(raw_input(), 'r') as finput:
        print(aes_128_ecb_decrypt(finput.read().decode('base64'), key))


def aes_128_ecb_decrypt(cipher_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(cipher_text);


def aes_128_ecb_encrypt(plain_text, key):
    plain_text = pad(plain_text, len(key))
    cipher = AES.new(key, AES.MODE_ECB)
    remainder = len(plain_text) % 16
    if remainder != 0:
        plain_text = str(plain_text + bytearray([16-remainder])*(16-remainder))
    return cipher.encrypt(plain_text)


if __name__ == "__main__": main()
