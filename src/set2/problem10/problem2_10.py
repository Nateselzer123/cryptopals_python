from src.set1.problem2.problem1_2 import xor
from src.set2.problem9.problem2_9 import pad
from src.set1.problem7.problem1_7 import aes_128_ecb_encrypt, aes_128_ecb_decrypt


def main():
    print("Enter file to decrypt:")
    finput = raw_input()
    print("Enter key:")
    key = raw_input()
    with open(finput, "r") as finput:
        plain_text = finput.read().decode('base64')
        print(cbc_decrypt(plain_text, key))


def cbc_encrypt(plain_text, key, init_vector=b"\x00"*16):

    block_start_index = 0
    block_size = len(key)
    cipher_text = b''
    cipher_text_block = init_vector
    plain_text = pad(plain_text, block_size)

    while block_start_index + block_size < len(plain_text):
        plain_text_block = plain_text[block_start_index:block_start_index+block_size]
        xord = xor(cipher_text_block, plain_text_block)
        cipher_text_block = aes_128_ecb_encrypt(xord, key)
        cipher_text += cipher_text_block
        block_start_index += block_size

    return cipher_text


def cbc_decrypt(cipher_text, key, init_vector=b"\x00"*16):
    block_size = len(key)
    block_start_index = 0
    prev_cipher_text_block = init_vector
    plain_text = b''
    while block_start_index < len(cipher_text) - block_size:
        cipher_text_block = cipher_text[block_start_index:block_start_index+block_size]
        xord = aes_128_ecb_decrypt(cipher_text_block, key)
        plain_text_block = xor(xord, prev_cipher_text_block)
        plain_text += plain_text_block
        block_start_index += block_size
        prev_cipher_text_block = cipher_text_block

    return plain_text


if __name__ == "__main__":
    main()
