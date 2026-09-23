"""Catalan number 10."""

def catalan(n):
    from math import comb
    return comb(2 * n, n) // (n + 1)

if __name__ == "__main__":
    assert catalan(10) == 16796
    print("ok")
