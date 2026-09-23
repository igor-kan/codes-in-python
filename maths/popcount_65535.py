"""Population count of 65535."""

def popcount(n):
    return bin(n).count('1')

if __name__ == "__main__":
    assert popcount(65535) == 16
    print("ok")
