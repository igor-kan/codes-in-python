"""Factorial of 25."""

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == "__main__":
    assert factorial(25) == 15511210043330985984000000
    print("ok")
