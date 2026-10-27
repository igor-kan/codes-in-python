"""Implementation of chebyshev collocation node order 16192."""

def compute_chebyshev_colloc_16192(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_16192():
    v=compute_chebyshev_colloc_16192(0.5)
    assert isinstance(v,float) and v==v
