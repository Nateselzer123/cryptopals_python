def main():
    print("Enter unpadded string:")
    unpadded = raw_input()
    print("Enter block size")
    block_size = input()
    # Print as byte-array to see non-ascii characters
    print(repr(pad(unpadded, block_size)))



def pad(unpadded, block_size):
    pad_length = block_size - len(unpadded) % block_size
    if pad_length == 0:
        pad_length = block_size
    padded_string = bytes(unpadded + bytearray([pad_length]*pad_length))
    return padded_string


if __name__ == "__main__":
    main()
