"""Factorial of 18."""

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == "__main__":
    assert factorial(18) == 6402373705728000
    print("ok")
