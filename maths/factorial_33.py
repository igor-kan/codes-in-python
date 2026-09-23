"""Factorial of 33."""

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == "__main__":
    assert factorial(33) == 8683317618811886495518194401280000000
    print("ok")
