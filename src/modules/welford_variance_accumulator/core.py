/**
 * @file core.py
 * @brief Welford numerically stable one-pass running mean and variance algorithm for Welford Numerically Stable Mean and Variance.
 * Module: welford_variance_accumulator
 */

#include "types.py"
#include <math.h>

typedef struct welford_variance_accumulator_welford {
    size_t count;
    double mean;
    double m2;
} welford_variance_accumulator_welford_t;

void welford_variance_accumulator_update(welford_variance_accumulator_welford_t* w, double x) {
    if (!w) return;
    w->count += 1;
    double delta = x - w->mean;
    w->mean += delta / (double)w->count;
    double delta2 = x - w->mean;
    w->m2 += delta * delta2;
}

double welford_variance_accumulator_variance(const welford_variance_accumulator_welford_t* w) {
    return (w && w->count > 1) ? (w->m2 / (double)(w->count - 1)) : 0.0;
}
