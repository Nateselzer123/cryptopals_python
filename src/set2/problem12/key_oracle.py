import os
from src.set1.problem7.problem1_7 import aes_128_ecb_encrypt


class KeyOracle:
    def __init__(
            self,
            block_size = 16,
            cipher_text = """Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
            aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
            dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
            YnkK"""
    ):
        self.key = os.urandom(block_size)
        self.cipher_text = cipher_text

    def ecb_encrypt_consistent_key(self, my_string):
        return aes_128_ecb_encrypt(my_string + self.cipher_text.decode('base64'), self.key)



