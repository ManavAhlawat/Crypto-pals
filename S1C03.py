char_frequency = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}


def get_score(input):
    
    s = 0

    for byte in input:
        s += char_frequency.get(chr(byte).lower(), 0)

    return s


def singlecharXOR(input, key):

    output = b''

    for char in input:
        output += bytes([char ^ key])

    return output


def singlecharXOR_brute_force(ciphertext):
    
    candidates = []

    for key_candidate in range(256):
        plaintext_candidate = singlecharXOR(ciphertext, key_candidate)
        candidate_score = get_score(plaintext_candidate)

        result = {
            'key': key_candidate,
            's': candidate_score,
            'plaintext': plaintext_candidate
        }

        candidates.append(result)

    return sorted(candidates, key=lambda c: c['s'], reverse=True)[0]


def pretty_print_result(result):
    print(result['plaintext'].decode().rstrip(), "\ts:", "{0:.2f}".format(result['s']),
          "\tKey:", chr(result['key']))


def main():
    ciphertext = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    most_likely_plaintext = singlecharXOR_brute_force(ciphertext)
    pretty_print_result(most_likely_plaintext)

    
    print (most_likely_plaintext['plaintext'].rstrip())


if __name__ == "__main__":
    main()