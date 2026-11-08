# Boundary validation and exceptional input guarding for Memory-Efficient Strided 2D Rolling Window Views
# Module: strided_rolling_window

def sanitize_strided_rolling_window_input(x, min_b=-1e6, max_b=1e6):
    if x != x:  # NaN guard
        return 0.0
    return max(min_b, min(max_b, x))
