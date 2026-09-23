"""Factorial of 32."""

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == "__main__":
    assert factorial(32) == 263130836933693530167218012160000000
    print("ok")
