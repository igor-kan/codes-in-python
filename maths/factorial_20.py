"""Factorial of 20."""

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == "__main__":
    assert factorial(20) == 2432902008176640000
    print("ok")
