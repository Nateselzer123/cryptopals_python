def main():
    print("Enter unpadded string:")
    unpadded = raw_input()
    print("Enter block size")
    block_size = input()
    print(pad(unpadded, block_size))


def pad(unpadded, block_size):
    pad_length = block_size - len(unpadded) % block_size
    padded_string = unpadded + bytes(pad_length)*pad_length
    return padded_string


if __name__ == "__main__":
    main()
