from binascii import hexlify


def repeating_key_xor(plaintext, key):
    ciphertext = b''
    i = 0

    for byte in plaintext:
        ciphertext += bytes([byte ^ key[i]])

        i = i + 1 if i < len(key) - 1 else 0

    return ciphertext


def main():
    c = repeating_key_xor(b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal", b'ICE')
    print ((str(hexlify(c), "utf-8")))
                                      


if __name__ == "__main__":
    main()