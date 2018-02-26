import heapq

english_freqs = {
            'a': 0.08167,
            'b': 0.01492,
            'c': 0.02782,
            'd': 0.04253,
            'e': 0.12702,
            'f': 0.02228,
            'g': 0.02015,
            'h': 0.06094,
            'i': 0.06966,
            'j': 0.00153,
            'k': 0.00772,
            'l': 0.04025,
            'm': 0.02406,
            'n': 0.06749,
            'o': 0.07507,
            'p': 0.01929,
            'q': 0.00095,
            'r': 0.05987,
            's': 0.06327,
            't': 0.09056,
            'u': 0.02758,
            'v': 0.00978,
            'w': 0.02360,
            'x': 0.00150,
            'y': 0.01974,
            'z': 0.00074,
            ' ': 0.19181,
            'other': .00001
}


def main():
    print("Enter your input string")
    input_bytes = raw_input().decode('hex')
    print(single_byte_decrypt_top_k(input_bytes, 5))


def single_byte_decrypt(input_bytes):

    input_byte_array = bytearray(input_bytes)

    low_score = float('inf')
    best_decrypted_string = ''

    for byte_key in range(0, 255):

        xord_byte_array = single_byte_xor(byte_key, input_byte_array)
        string_score = score(xord_byte_array)

        if string_score < low_score:
            low_score = string_score
            best_decrypted_string = ''.join(xord_byte_array)

    return best_decrypted_string, low_score


def single_byte_decrypt_top_k(input_bytes, k):

    input_byte_array = bytearray(input_bytes)
    low_score_heap = [(-float('inf'), '')]

    for byte_key in range(0, 255):

        xord_byte_array = single_byte_xor(byte_key, input_byte_array)
        string_score = score(xord_byte_array)
        negative_string_score = -string_score

        if negative_string_score > low_score_heap[0][0]:
            heapq.heappush(low_score_heap, (negative_string_score, xord_byte_array))
            if len(low_score_heap) > k:
                heapq.heappop(low_score_heap)

    top_k = [(''.join(ba), -negative_string_score) for (negative_string_score, ba) in low_score_heap]
    top_k.reverse()
    return top_k


def single_byte_xor(byte_key, input_bytes):
    return [chr(byte_key ^ input_byte) for input_byte in input_bytes]


def score(s):

    count = {key: 0 for key, val in english_freqs.items()}

    for c in s:
        c = c.lower()
        if c in english_freqs:
            count[c] += 1
        else:
            count['other'] += 1

    string_score = 0

    for c in range(ord('a'), ord('z')+1):
        c = chr(c)
        expected = english_freqs[c]*float(len(s))
        difference = count[c]-expected
        string_score += float(difference*difference)/expected

    string_score += count['other']**2/english_freqs['other']/float(len(s))

    return string_score


if __name__ == "__main__":
    main()
