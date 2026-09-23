"""Reverse digits of 123."""

def reverse_int(n):
    s = str(abs(n))
    return int(s[::-1]) * (-1 if n < 0 else 1)

if __name__ == "__main__":
    assert reverse_int(123) == 321
    print("ok")
