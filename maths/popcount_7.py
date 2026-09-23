"""Population count of 7."""

def popcount(n):
    return bin(n).count('1')

if __name__ == "__main__":
    assert popcount(7) == 3
    print("ok")
