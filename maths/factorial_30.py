"""Factorial of 30."""

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == "__main__":
    assert factorial(30) == 265252859812191058636308480000000
    print("ok")
