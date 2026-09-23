"""Digit sum of 31415926."""

def digit_sum(n):
    return sum(int(c) for c in str(abs(n)))

if __name__ == "__main__":
    assert digit_sum(31415926) == 31
    print("ok")
