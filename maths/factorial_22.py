"""Factorial of 22."""

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == "__main__":
    assert factorial(22) == 1124000727777607680000
    print("ok")
