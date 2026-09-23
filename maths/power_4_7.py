"""Raise 4 to the 7."""

def power(a, b):
    r = 1
    for _ in range(b):
        r *= a
    return r

if __name__ == "__main__":
    assert power(4, 7) == 16384
    print("ok")
