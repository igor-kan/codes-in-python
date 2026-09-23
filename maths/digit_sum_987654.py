"""Digit sum of 987654."""

def digit_sum(n):
    return sum(int(c) for c in str(abs(n)))

if __name__ == "__main__":
    assert digit_sum(987654) == 39
    print("ok")
