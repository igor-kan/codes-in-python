"""Factorial of 27."""

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == "__main__":
    assert factorial(27) == 10888869450418352160768000000
    print("ok")
