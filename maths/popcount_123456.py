"""Population count of 123456."""

def popcount(n):
    return bin(n).count('1')

if __name__ == "__main__":
    assert popcount(123456) == 6
    print("ok")
