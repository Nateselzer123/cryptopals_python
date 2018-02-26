from src.set1.problem3.problem1_3 import *
import heapq

def main():
    print("Input number of tries")
    k = input()
    print("Input file name:")
    with open(raw_input(), 'rb') as finput:
        print(detect_single_byte_xor_top_k(finput, k))


def detect_single_byte_xor_top_k(finput, k):
    top_k_decrypted_strings = [(-float('inf'), '')]
    num_lines = 0
    for line in finput:
        line = line.strip().decode('hex')
        for good_string, good_score in single_byte_decrypt_top_k(line, k):
            if -good_score > top_k_decrypted_strings[0][0]:
                heapq.heappush(top_k_decrypted_strings, (-good_score, good_string))
                if len(top_k_decrypted_strings) > k:
                    heapq.heappop(top_k_decrypted_strings)

    top_k = [(''.join(ba), -negative_string_score) for (negative_string_score, ba) in top_k_decrypted_strings]
    top_k.reverse()
    return top_k


if __name__ == "__main__":
    main()

