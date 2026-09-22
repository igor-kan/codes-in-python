def hamming_distance(a, b):
    return bin(a ^ b).count("1")

if __name__ == "__main__":
    assert hamming_distance(1, 4) == 2
    assert hamming_distance(7, 7) == 0
    print("ok")
