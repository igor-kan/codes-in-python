def bisection(f, a, b, tol=1e-12, iters=200):
    fa = f(a)
    for _ in range(iters):
        m = 0.5 * (a + b); fm = f(m)
        if abs(b - a) < tol or fm == 0: return m
        if fa * fm < 0: b = m
        else: a, fa = m, fm
    return 0.5 * (a + b)

if __name__ == "__main__":
    r = bisection(lambda x: x*x - 2, 0, 2)
    assert abs(r - 2**0.5) < 1e-9
    print("ok")
