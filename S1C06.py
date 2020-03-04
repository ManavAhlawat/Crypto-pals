from base64 import b64decode
from S1C03 import singlecharXOR_brute_force, get_score
from S1C05 import repeating_key_xor
from itertools import combinations


def distance_hamming(binary_1, binary_2):
    
    assert len(binary_1) == len(binary_2)
    dist = 0

    for bit1, bit2 in zip(binary_1, binary_2):
        diff = bit1 ^ bit2
        dist += sum([1 for bit in bin(diff) if bit == '1'])

    return dist


def breakRepeatingKeyXor(binary_data):

    norm_dists = {}

  
    for key_size in range(2, 41):

        
        parts = [binary_data[i:i + key_size] for i in range(0, len(binary_data), key_size)][:4]

        distance = 0
        pairs = combinations(parts, 2)
        for (x, y) in pairs:
            distance += distance_hamming(x, y)

    
        distance /= 6

        
        norm_dist = distance / key_size

    
        norm_dists[key_size] = norm_dist

    
    keySizes_possible = sorted(norm_dists, key=norm_dists.get)[:3]
    possible_plaintexts = []

    for d in keySizes_possible:
        key = b''

        for i in range(d):
            block = b''

            
            for j in range(i, len(binary_data), d):
                block += bytes([binary_data[j]])

            
            key += bytes([singlecharXOR_brute_force(block)['key']])

       
        possible_plaintexts.append((repeating_key_xor(binary_data, key), key))

   
    return max(possible_plaintexts, key=lambda k: get_score(k[0]))


def main():

   
    print (distance_hamming(b'this is a test', b'wokka wokka!!!'))

    with open("S1C06_input.txt") as input_file:
        data = b64decode(input_file.read())

   
    result = breakRepeatingKeyXor(data)
    print("Key =", result[1].decode())
    print("---------------------------------------")
    print(result[0].decode().rstrip())


if __name__ == "__main__":
    main()