def sqrt_newton(x, tol=1e-12):
    if x < 0: raise ValueError
    if x == 0: return 0.0
    g = x
    while abs(g * g - x) > tol:
        g = 0.5 * (g + x / g)
    return g

if __name__ == "__main__":
    assert abs(sqrt_newton(2) - 2**0.5) < 1e-12
    print("ok")
