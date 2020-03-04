from S1C03 import singlecharXOR_brute_force, pretty_print_result


def detect_encrypted_text(encrypted_strings):
    
    candidates = []

    for string in encrypted_strings:
        candidates.append(singlecharXOR_brute_force(string))

    return sorted(candidates, key=lambda c: c['s'], reverse=True)[0]


def main():
    ciphertexts = [bytes.fromhex(line.strip()) for line in open("S1C04_input.txt")]
    most_likely_plaintext = detect_encrypted_text(ciphertexts)
    pretty_print_result(most_likely_plaintext)
    print(most_likely_plaintext['plaintext'].rstrip())

if __name__ == "__main__":
    main()