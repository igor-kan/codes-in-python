"""Factorial of 38."""

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == "__main__":
    assert factorial(38) == 523022617466601111760007224100074291200000000
    print("ok")
