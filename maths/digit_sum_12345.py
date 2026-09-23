"""Digit sum of 12345."""

def digit_sum(n):
    return sum(int(c) for c in str(abs(n)))

if __name__ == "__main__":
    assert digit_sum(12345) == 15
    print("ok")
