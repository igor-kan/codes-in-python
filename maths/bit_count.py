def popcount(n):
    c = 0
    while n:
        n &= n - 1; c += 1
    return c

if __name__ == "__main__":
    assert popcount(0b101101) == 4
    assert popcount(0) == 0
    print("ok")
