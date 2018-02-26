import base64
from Crypto.Cipher import AES


def main():
    print("Key:")
    key=raw_input().decode('utf-8')
    print("Input file:")
    with open(raw_input(), 'r') as finput:
            print(aes_128_ecb_decrypt(key, finput))


def aes_128_ecb_decrypt(key, finput):
    b = finput.read().decode('base64')
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(b);


def aes_128_ecb_encrypt(key, finput):
    b = finput.read()
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(b).encode('base64')

if __name__ == "__main__": main()
