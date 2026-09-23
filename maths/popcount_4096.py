"""Population count of 4096."""

def popcount(n):
    return bin(n).count('1')

if __name__ == "__main__":
    assert popcount(4096) == 1
    print("ok")
