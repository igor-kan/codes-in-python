from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    assert fib(10) == 55
    assert fib(0) == 0
    print("ok")
