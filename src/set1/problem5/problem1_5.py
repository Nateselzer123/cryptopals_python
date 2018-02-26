def main():
    print("Enter your string")
    s = raw_input()
    print("Enter your key")
    key = raw_input()
    print(repeating_key_xor(s, key))


def repeating_key_xor(s, key):
    xord = []
    index = 0
    for c in s:
        xord += chr(ord(c) ^ ord(key[index % len(key)]))
        index += 1
    return ''.join(xord).encode('hex')


if __name__ == "__main__":
    main()

