def trapezoidal(f, a, b, n=1000):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b)) + sum(f(a + i * h) for i in range(1, n))
    return s * h

if __name__ == "__main__":
    import math
    assert abs(trapezoidal(math.sin, 0, math.pi) - 2.0) < 1e-3
    print("ok")
