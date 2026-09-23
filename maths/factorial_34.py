"""Factorial of 34."""

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == "__main__":
    assert factorial(34) == 295232799039604140847618609643520000000
    print("ok")
