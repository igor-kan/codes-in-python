"""Factorial of 29."""

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == "__main__":
    assert factorial(29) == 8841761993739701954543616000000
    print("ok")
