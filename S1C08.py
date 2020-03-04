from Crypto.Cipher.AES import block_size


def cnt_aes_ecb_repeat(ciphertext):
    parts = [ciphertext[i:i + block_size] for i in range(0, len(ciphertext), block_size)]
    no_duplicate = len(parts) - len(set(parts))
    return no_duplicate


def detect_ecb_encrypted_ciphertext(ciphertexts):
    best = (-1, 0)   

    for i in range(len(ciphertexts)):

        repetitions = cnt_aes_ecb_repeat(ciphertexts[i])

        best = max(best, (i, repetitions), key=lambda t: t[1])

    return best


def main():
    ciphertexts = [bytes.fromhex(line.strip()) for line in open("S1C08_input.txt")]
    result = detect_ecb_encrypted_ciphertext(ciphertexts)

    print("The ciphertext encrypted in ECB mode is the one at position", result[0],
          "which contains", result[1], "repetitions")

    print (result[0])


if __name__ == "__main__":
    main()