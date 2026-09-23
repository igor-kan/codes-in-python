"""Raise 7 to the 3."""

def power(a, b):
    r = 1
    for _ in range(b):
        r *= a
    return r

if __name__ == "__main__":
    assert power(7, 3) == 343
    print("ok")
