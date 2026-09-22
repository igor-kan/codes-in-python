def is_armstrong(n):
    digits = str(n)
    return n == sum(int(d) ** len(digits) for d in digits)

if __name__ == "__main__":
    assert is_armstrong(153)
    assert not is_armstrong(100)
    print("ok")
