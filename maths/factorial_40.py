"""Factorial of 40."""

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == "__main__":
    assert factorial(40) == 815915283247897734345611269596115894272000000000
    print("ok")
