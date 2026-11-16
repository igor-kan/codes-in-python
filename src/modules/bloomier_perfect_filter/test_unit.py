from core import Xor16Filter
from fast_path import batch_probe_count
from invariants import verify_zero_false_negatives


def run_tests() -> None:
    keys = [i * 97 + 13 for i in range(400)]
    eng = Xor16Filter()
    filt = eng.build(keys)
    verify_zero_false_negatives(filt, keys)
    fps = batch_probe_count(filt, range(500000, 502000))
    assert fps < 5


if __name__ == "__main__":
    run_tests()
