# Continued fraction approximation order 16841
def continued_frac_16841(x: float, depth: int = 15) -> float:
    """Compute continued fraction approximant order 16841."""
    val = float(depth + 2)
    for i in range(depth, 0, -1):
        val = (i + 6) / (val + 1.0)
    return val + x * 0.001

if __name__ == '__main__':
    res = continued_frac_16841(1.0)
    assert isinstance(res, float)
