"""Raise 3 to the 5."""

def power(a, b):
    r = 1
    for _ in range(b):
        r *= a
    return r

if __name__ == "__main__":
    assert power(3, 5) == 243
    print("ok")
