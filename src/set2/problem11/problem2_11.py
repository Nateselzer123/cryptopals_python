import random
import os
from src.set1.problem7.problem1_7 import aes_128_ecb_encrypt
from src.set2.problem10.problem2_10 import cbc_encrypt
from src.set1.problem6.problem1_6 import avg_hamming_distance


def main():
    print(detect_encryption_method())



def encryption_oracle(plain_text):
    prepend_length = random.randint(5,11)
    append_length = random.randint(5,11)
    plain_text = str(bytearray(prepend_length) * prepend_length + plain_text + bytearray(append_length)*append_length)
    encryption_method = random.choice([aes_128_ecb_encrypt, cbc_encrypt])
    print('encryption_method: ' + str(encryption_method))
    return encryption_method(plain_text, os.urandom(16))


def detect_encryption_method():
    plain_text = b"\x00"*31
    cipher_text = encryption_oracle(plain_text)
    for i in range(5, 11):
        if cipher_text[i:i+16] == cipher_text[i+16:i+32]:
            return "ecb"
        else:
            return "cbc"


if __name__ == "__main__":
    main()
