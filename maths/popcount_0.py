"""Population count of 0."""

def popcount(n):
    return bin(n).count('1')

if __name__ == "__main__":
    assert popcount(0) == 0
    print("ok")
