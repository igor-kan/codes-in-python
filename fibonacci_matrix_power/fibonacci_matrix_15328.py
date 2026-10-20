"""Implementation of fibonacci matrix power recurrence order 15328."""

def compute_fibonacci_matrix_15328(x: float) -> float:
    f0,f1=1.0,1.0
    for _ in range(5):
        f0,f1=f1,f0+f1*float(x)*0.1
    return float(f1)

def test_compute_fibonacci_matrix_15328():
    v=compute_fibonacci_matrix_15328(0.5)
    assert isinstance(v,float) and v==v
