"""Factorial of 35."""

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == "__main__":
    assert factorial(35) == 10333147966386144929666651337523200000000
    print("ok")
