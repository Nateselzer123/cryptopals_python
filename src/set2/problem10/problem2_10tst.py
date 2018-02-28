from problem2_10 import cbc_encrypt, cbc_decrypt


def main():
    with open("2-10tst.txt", 'r') as finput:
        print(len("DIONNE WARWICK  "))
        cipher_text = cbc_encrypt(finput.read(), "DIONNE WARWICK  ")
        print("cipher text", cipher_text)
        plain_text = cbc_decrypt(cipher_text, "DIONNE WARWICK  ")
        print("plain text", plain_text)


if __name__ == "__main__":
    main()