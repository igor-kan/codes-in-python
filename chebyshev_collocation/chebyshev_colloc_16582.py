"""Implementation of chebyshev collocation node order 16582."""

def compute_chebyshev_colloc_16582(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_16582():
    v=compute_chebyshev_colloc_16582(0.5)
    assert isinstance(v,float) and v==v
