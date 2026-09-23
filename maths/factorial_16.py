"""Factorial of 16."""

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == "__main__":
    assert factorial(16) == 20922789888000
    print("ok")
