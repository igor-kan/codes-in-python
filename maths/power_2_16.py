"""Raise 2 to the 16."""

def power(a, b):
    r = 1
    for _ in range(b):
        r *= a
    return r

if __name__ == "__main__":
    assert power(2, 16) == 65536
    print("ok")
