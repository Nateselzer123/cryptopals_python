from Crypto.Cipher import AES
from src.set1.problem6.problem1_6 import avg_hamming_distance
from src.set1.problem7.problem1_7 import aes_128_ecb_decrypt


def main():
    print("Input file:")
    with open(raw_input(), 'r') as finput:
        print(aes_128_ecb_detect(finput))


def aes_128_ecb_detect(finput):
    min_avg_hamming_distance = float('inf')
    aes_string = ''
    for line in finput:
        line = line.strip().decode('hex')
        dist = avg_hamming_distance(line, 16)
        if dist < min_avg_hamming_distance:
            min_avg_hamming_distance = dist
            aes_string = line
    return aes_string.encode('hex')


if __name__ == "__main__": main()