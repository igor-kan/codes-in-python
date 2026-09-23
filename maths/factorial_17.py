"""Factorial of 17."""

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == "__main__":
    assert factorial(17) == 355687428096000
    print("ok")
