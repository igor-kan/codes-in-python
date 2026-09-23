"""Raise 5 to the 4."""

def power(a, b):
    r = 1
    for _ in range(b):
        r *= a
    return r

if __name__ == "__main__":
    assert power(5, 4) == 625
    print("ok")
