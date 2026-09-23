"""Raise 10 to the 6."""

def power(a, b):
    r = 1
    for _ in range(b):
        r *= a
    return r

if __name__ == "__main__":
    assert power(10, 6) == 1000000
    print("ok")
