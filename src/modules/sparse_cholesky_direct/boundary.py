# Boundary validation and exceptional input guarding for Direct Sparse Cholesky Solver with Fill-Reducing Order
# Module: sparse_cholesky_direct

def sanitize_sparse_cholesky_direct_input(x, min_v=-1e6, max_v=1e6):
    if x != x:
        return 0.0
    return max(min_v, min(max_v, x))
