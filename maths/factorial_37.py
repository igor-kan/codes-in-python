"""Factorial of 37."""

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == "__main__":
    assert factorial(37) == 13763753091226345046315979581580902400000000
    print("ok")
