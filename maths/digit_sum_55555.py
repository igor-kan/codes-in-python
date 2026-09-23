"""Digit sum of 55555."""

def digit_sum(n):
    return sum(int(c) for c in str(abs(n)))

if __name__ == "__main__":
    assert digit_sum(55555) == 25
    print("ok")
