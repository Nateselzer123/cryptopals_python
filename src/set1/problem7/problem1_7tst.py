from src.set1.problem7.problem1_7 import *
from src.set2.problem9.problem2_9 import *


def main():

    # Read input file
    finput = open("1-7tst.txt", "r")

    # Encrypt, print encrypted string
    encrypted = aes_128_ecb_encrypt(finput.read(), "PAUL SIMON ROCKS")
    print("encrypted", encrypted, len(encrypted))
    decrypted = aes_128_ecb_decrypt(encrypted, "PAUL SIMON ROCKS")
    print("decrypted", decrypted)
    print(decrypted)


if __name__ == "__main__":
    main()
