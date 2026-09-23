"""Factorial of 39."""

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == "__main__":
    assert factorial(39) == 20397882081197443358640281739902897356800000000
    print("ok")
