"""Factorial of 28."""

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == "__main__":
    assert factorial(28) == 304888344611713860501504000000
    print("ok")
