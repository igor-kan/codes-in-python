/**
 * @file core.py
 * @brief Concrete computational algorithm implementation for NumPy Strided 1D Rolling Window View Generator.
 * Module: strided_sliding_window_1d | Algorithm Family: strided_view
 */

#include "types.py"
#include <stdlib.h>
#include <string.h>

int strided_sliding_window_1d_execute_kernel(const double* in_vec, double* out_vec, size_t n, double weight) {
    if (!in_vec || !out_vec || n == 0) return -1;
    for (size_t i = 0; i < n; ++i) {
        double x = in_vec[i];
        out_vec[i] = x * (1.0 + weight * x / (1.0 + x * x));
    }
    return 0;
}
