import math
from bitstring import BitArray
import heapq
from src.set1.problem3.problem1_3 import single_byte_decrypt


MAX_COMPARISONS = 1000


def main():
    print("Enter file with base64 encrypted string")
    with open(raw_input(), 'rb') as finput:
        input_bytes = finput.read().decode('base64')
        print("Enter number of tries")
        k = input()
        print(break_repeating_key_xor(input_bytes.encode('utf-8'), k))


def break_repeating_key_xor(input_bytes, k):
    final_strings = []
    for key_size, _ in key_sizes_top_k(input_bytes, k):
        block_set_unsolved = transpose(input_bytes, key_size)
        block_set_solved = []
        for block in block_set_unsolved:
            block_set_solved.append(single_byte_decrypt(block)[0])
        final_strings.append(untranspose(block_set_solved))

    return final_strings


def untranspose(block_set):
    final_string = ''
    index = 0
    while True:
        for block in block_set:
            if index >= len(block):
                return final_string
            final_string += block[index]
        index += 1


def transpose(s, key_size):
    blocks = []
    for i in range(key_size):
        blocks.append(s[i::key_size])

    return blocks


def key_sizes_top_k(s, k):
    # (normalized_hamming_distance, key_size)
    top_k_key_sizes = [(float(-8), 0)]

    for i in range(2, 40):
        if i >= len(s)/2:
            break
        dist = avg_hamming_distance(s, i)
        if -dist > top_k_key_sizes[0][0]:
            heapq.heappush(top_k_key_sizes, (-dist, i))
            if len(top_k_key_sizes) > k:
                heapq.heappop(top_k_key_sizes)

    top_k = [(key_size, -negative_normalized_hamming_dist) for
             (negative_normalized_hamming_dist, key_size) in top_k_key_sizes]
    top_k.reverse()
    return top_k


def avg_hamming_distance(s, key_size):

    a = 0
    dist = 0
    divisor = 0

    while a + key_size < len(s):
        s1 = s[a:a + key_size]
        b= a + key_size
        while b + key_size < len(s):
            s2 = s[b:b + key_size]
            dist += hamming_distance(s1, s2)
            divisor += 1
            b += key_size
        a += key_size
        if divisor >= MAX_COMPARISONS:
            break

    return float(dist)/float(divisor)/float(key_size)


def hamming_distance(s1, s2):
    ba1 = BitArray(hex=s1.encode('hex'))
    ba2 = BitArray(hex=s2.encode('hex'))
    return (ba1 ^ ba2).count(1)


if __name__ == "__main__":
    main()