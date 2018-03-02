import random
import os
from src.set1.problem7.problem1_7 import aes_128_ecb_encrypt
from src.set2.problem10.problem2_10 import cbc_encrypt


def main():
    print(detect_encryption_method(encryption_oracle))


def encryption_oracle(plain_text):
    prepend_length = random.randint(5,11)
    append_length = random.randint(5,11)
    plain_text = str(bytearray(prepend_length) * prepend_length + plain_text + bytearray(append_length)*append_length)
    encryption_method = random.choice([aes_128_ecb_encrypt, cbc_encrypt])
    print(encryption_method)
    return encryption_method(plain_text, os.urandom(16))


def detect_encryption_method(mystery_encryption, block_size = 16):
    plain_text = b"\x00"*2*block_size
    cipher_text = mystery_encryption(plain_text)
    for i in range(0, 32):
        if i + 2 * block_size >= len(cipher_text):
            break
        if cipher_text[i:i+block_size] == cipher_text[i+block_size:i+2*block_size]:
            return "ecb"

    return "cbc"


if __name__ == "__main__":
    main()
