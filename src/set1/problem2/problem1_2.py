def main():
    print("Enter your first hex string")
    hex1 = raw_input()
    print("Enter your second hex string")
    hex2 = raw_input()
    print(xor(hex1.decode("hex"), hex2.decode("hex")))


def xor(s1, s2):
    return ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2)]).encode('hex')


if __name__ == "__main__": main()
