/**
 * @file core.py
 * @brief Welford numerically stable one-pass running mean and variance algorithm for Welford One-Pass Numerically Stable Mean and Variance.
 * Module: welford_running_variance
 */

#include "types.py"

typedef struct welford_running_variance_accumulator {
    size_t count;
    double mean;
    double m2;
} welford_running_variance_accumulator_t;

void welford_running_variance_push(welford_running_variance_accumulator_t* acc, double val) {
    if (!acc) return;
    acc->count += 1;
    double delta = val - acc->mean;
    acc->mean += delta / (double)acc->count;
    double delta2 = val - acc->mean;
    acc->m2 += delta * delta2;
}

double welford_running_variance_get_variance(const welford_running_variance_accumulator_t* acc) {
    return (acc && acc->count > 1) ? (acc->m2 / (double)(acc->count - 1)) : 0.0;
}
