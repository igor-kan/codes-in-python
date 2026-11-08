# Boundary validation and exceptional input guarding for C-Contiguous Fast Matrix-Vector Multiplication
# Module: cython_fast_gemv

def sanitize_cython_fast_gemv_input(x, min_b=-1e6, max_b=1e6):
    if x != x:  # NaN guard
        return 0.0
    return max(min_b, min(max_b, x))
