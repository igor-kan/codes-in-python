"""Population count of 256."""

def popcount(n):
    return bin(n).count('1')

if __name__ == "__main__":
    assert popcount(256) == 1
    print("ok")
