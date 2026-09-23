"""Digit sum of 2024."""

def digit_sum(n):
    return sum(int(c) for c in str(abs(n)))

if __name__ == "__main__":
    assert digit_sum(2024) == 8
    print("ok")
