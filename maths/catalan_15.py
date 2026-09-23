"""Catalan number 15."""

def catalan(n):
    from math import comb
    return comb(2 * n, n) // (n + 1)

if __name__ == "__main__":
    assert catalan(15) == 9694845
    print("ok")
