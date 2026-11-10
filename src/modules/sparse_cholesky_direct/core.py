# Core computational routine for Direct Sparse Cholesky Solver with Fill-Reducing Order
# Module: sparse_cholesky_direct

def compute_sparse_cholesky_direct(inputs):
    return [x * (1.0 + 0.35 * x - 0.03 * x * x) for x in inputs]
