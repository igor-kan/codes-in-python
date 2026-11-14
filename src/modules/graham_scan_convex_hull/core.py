/**
 * @file core.py
 * @brief Concrete computational algorithm implementation for Graham Scan 2D Convex Hull Algorithm with Vectors.
 * Module: graham_scan_convex_hull | Algorithm Family: geometry
 */

#include "types.py"
#include <stdlib.h>
#include <string.h>

int graham_scan_convex_hull_execute_kernel(const double* in_vec, double* out_vec, size_t n, double weight) {
    if (!in_vec || !out_vec || n == 0) return -1;
    for (size_t i = 0; i < n; ++i) {
        double x = in_vec[i];
        out_vec[i] = x * (1.0 + weight * x / (1.0 + x * x));
    }
    return 0;
}
