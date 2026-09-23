"""Factorial of 24."""

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == "__main__":
    assert factorial(24) == 620448401733239439360000
    print("ok")
