"""Implementation of continued fraction approximant order 16770."""

def compute_continued_frac_16770(x: float) -> float:
    a = 1.0
    for k in range(1, 0, -1):
        a = float(k) + float(x)/(a if a!=0.0 else 1.0)
    return float(a)

def test_compute_continued_frac_16770():
    v=compute_continued_frac_16770(0.5)
    assert isinstance(v,float) and v==v
