"""Population count of 1."""

def popcount(n):
    return bin(n).count('1')

if __name__ == "__main__":
    assert popcount(1) == 1
    print("ok")
