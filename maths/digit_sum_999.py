"""Digit sum of 999."""

def digit_sum(n):
    return sum(int(c) for c in str(abs(n)))

if __name__ == "__main__":
    assert digit_sum(999) == 27
    print("ok")
