def is_perfect(n):
    if n < 2: return False
    return sum(d for d in range(1, n) if n % d == 0) == n

if __name__ == "__main__":
    assert is_perfect(28)
    assert not is_perfect(12)
    print("ok")
