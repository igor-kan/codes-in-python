"""Reverse digits of 98765."""

def reverse_int(n):
    s = str(abs(n))
    return int(s[::-1]) * (-1 if n < 0 else 1)

if __name__ == "__main__":
    assert reverse_int(98765) == 56789
    print("ok")
