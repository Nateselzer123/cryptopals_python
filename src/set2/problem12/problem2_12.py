import random
import os
from src.set1.problem7.problem1_7 import aes_128_ecb_encrypt
from src.set2.problem10.problem2_10 import cbc_encrypt
from src.set2.problem11.problem2_11 import detect_encryption_method
from key_oracle import KeyOracle


def main():
    oracle = KeyOracle(16)
    print(find_block_size(oracle))
    print(detect_encryption_method(oracle.ecb_encrypt_consistent_key))
    print(repr(build_block_dictionary(oracle, "A" * 15, "", 0, 16)))
    print(repr(ecb_decrypt(oracle, 16)))


def oracle_decrypt(oracle):
    block_size = find_block_size(oracle)
    encryption_method = detect_encryption_method(oracle.ecb_encrypt_consistent_key)
    if encryption_method == "ecb":
        ecb_decrypt(oracle, block_size)


def ecb_decrypt(oracle, block_size):
    plain_text = ''
    cipher_text_length_with_padding = len(oracle.ecb_encrypt_consistent_key(''))
    last_plain_text_block = ecb_decrypt_first_block(oracle, 0, block_size)
    plain_text += last_plain_text_block
    while len(plain_text) + block_size < cipher_text_length_with_padding:
        last_plain_text_block += ecb_decrypt_block(oracle, len(plain_text), block_size, last_plain_text_block)
        plain_text += last_plain_text_block


def ecb_decrypt_first_block(oracle, block_start_index, block_size):
    known_string = ''
    while len(known_string) != block_size:
        my_string = 'A' * (block_size - len(known_string) - 1)
        cipher_text = oracle.ecb_encrypt_consistent_key(my_string)
        cipher_block = cipher_text[block_start_index:block_start_index + block_size]
        cipher_text_block_dict = build_block_dictionary(oracle, my_string, known_string, block_start_index, block_size)
        found_letter = cipher_text_block_dict[cipher_block]
        known_string += found_letter
    print(known_string)
    return known_string


def ecb_decrypt_block(oracle, block_start_index, block_size, last_plain_text_block):
    known_string = ''
    while len(known_string) != block_size:
        my_string = 'A' * (block_size - len(known_string) - 1)
        cipher_text = oracle.ecb_encrypt_consistent_key(my_string)
        cipher_block = cipher_text[block_start_index:block_start_index + block_size]
        print("cipher_block", len(cipher_block))
        cipher_text_block_dict = build_block_dictionary(oracle,
                                                        last_plain_text_block[block_size - len(my_string): block_size],
                                                        known_string,
                                                        block_start_index,
                                                        block_size)
        found_letter = cipher_text_block_dict[cipher_block]
        known_string += found_letter
    print(known_string)
    return known_string


# After the first block is decrypted,
# my_string is actually the last few digits of the last plain_text_block to be decrypted
def build_block_dictionary(oracle, my_string, end_string, block_start_index, block_size):
    print(my_string, end_string, block_start_index, block_size)
    cipher_block_dict = {}
    for i in range(0, 256):
        print(str(my_string + end_string + bytearray([i])))
        cipher_text = oracle.ecb_encrypt_consistent_key(str(my_string + end_string + bytearray([i])))
        cipher_block_dict.update({cipher_text[block_start_index: block_start_index + block_size]:
                                      str(bytearray([i]))})

    print("cipher block dict", cipher_block_dict)
    return cipher_block_dict


# Note this doesn't work for key size 24. 24 case is a bit more tricky because you still have to pad the cipher text
# to multiples of 16.
def find_block_size(oracle):
    cipher_and_padding_length = len(oracle.ecb_encrypt_consistent_key(""))
    altered_string_length = cipher_and_padding_length
    my_string = ""
    while altered_string_length == cipher_and_padding_length:
        my_string += "A"
        altered_string_length = len(oracle.ecb_encrypt_consistent_key(my_string))

    return altered_string_length - cipher_and_padding_length


if __name__ == "__main__":
    main()
