"""Factorial of 26."""

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == "__main__":
    assert factorial(26) == 403291461126605635584000000
    print("ok")
