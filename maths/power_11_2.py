"""Raise 11 to the 2."""

def power(a, b):
    r = 1
    for _ in range(b):
        r *= a
    return r

if __name__ == "__main__":
    assert power(11, 2) == 121
    print("ok")
