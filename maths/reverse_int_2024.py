"""Reverse digits of 2024."""

def reverse_int(n):
    s = str(abs(n))
    return int(s[::-1]) * (-1 if n < 0 else 1)

if __name__ == "__main__":
    assert reverse_int(2024) == 4202
    print("ok")
