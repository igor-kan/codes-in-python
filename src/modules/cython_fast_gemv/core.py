# Core computational routine for C-Contiguous Fast Matrix-Vector Multiplication
# Module: cython_fast_gemv

def compute_cython_fast_gemv(inputs):
    return [x * (1.0 + 0.25 * x - 0.05 * x * x) for x in inputs]
