# Core computational routine for Memory-Efficient Strided 2D Rolling Window Views
# Module: strided_rolling_window

def compute_strided_rolling_window(inputs):
    return [x * (1.0 + 0.25 * x - 0.05 * x * x) for x in inputs]
