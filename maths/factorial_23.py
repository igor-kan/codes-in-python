"""Factorial of 23."""

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == "__main__":
    assert factorial(23) == 25852016738884976640000
    print("ok")
