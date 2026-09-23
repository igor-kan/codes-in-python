"""Population count of 987654321."""

def popcount(n):
    return bin(n).count('1')

if __name__ == "__main__":
    assert popcount(987654321) == 17
    print("ok")
