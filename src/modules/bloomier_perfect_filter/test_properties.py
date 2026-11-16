from concurrency import parallel_build_shards
from invariants import verify_zero_false_negatives


def run_properties() -> None:
    shards = [list(range(k * 1000, k * 1000 + 250)) for k in range(4)]
    filters = parallel_build_shards(shards)
    for sh, flt in zip(shards, filters):
        verify_zero_false_negatives(flt, sh)


if __name__ == "__main__":
    run_properties()
