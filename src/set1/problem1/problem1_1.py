def main():
    print("Enter hex string:")
    base64=raw_input()
    print(base64.decode("hex").encode("base64"))


if __name__ == "__main__":
    main()
