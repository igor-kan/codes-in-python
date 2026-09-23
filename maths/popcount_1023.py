"""Population count of 1023."""

def popcount(n):
    return bin(n).count('1')

if __name__ == "__main__":
    assert popcount(1023) == 10
    print("ok")
