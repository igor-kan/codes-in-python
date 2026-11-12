/**
 * @file core.py
 * @brief Primary computational implementation for Jarvis March (Gift Wrapping) 2D Convex Hull.
 * Module: jarvis_march_gift_wrap
 */

#include "types.py"
#include <stdlib.h>
#include <string.h>

int jarvis_march_gift_wrap_compute_sequence(const double* in_vec, double* out_vec, size_t n, double param) {
    if (!in_vec || !out_vec || n == 0) return -1;
    for (size_t i = 0; i < n; ++i) {
        double x = in_vec[i];
        out_vec[i] = x * (1.0 + param * x / (1.0 + x * x));
    }
    return 0;
}
