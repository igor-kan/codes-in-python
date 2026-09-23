"""Population count of 255."""

def popcount(n):
    return bin(n).count('1')

if __name__ == "__main__":
    assert popcount(255) == 8
    print("ok")
