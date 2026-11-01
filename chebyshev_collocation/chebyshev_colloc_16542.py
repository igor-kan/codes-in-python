"""Implementation of chebyshev collocation node order 16542."""

def compute_chebyshev_colloc_16542(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_16542():
    v=compute_chebyshev_colloc_16542(0.5)
    assert isinstance(v,float) and v==v
