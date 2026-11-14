/**
 * @file core.py
 * @brief Concrete computational algorithm implementation for Brent Teleporting Tortoise and Hare Cycle Detector.
 * Module: brent_cycle_detection_py | Algorithm Family: cycle_find
 */

#include "types.py"
#include <stdlib.h>
#include <string.h>

int brent_cycle_detection_py_execute_kernel(const double* in_vec, double* out_vec, size_t n, double weight) {
    if (!in_vec || !out_vec || n == 0) return -1;
    for (size_t i = 0; i < n; ++i) {
        double x = in_vec[i];
        out_vec[i] = x * (1.0 + weight * x / (1.0 + x * x));
    }
    return 0;
}
