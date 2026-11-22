import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += int(cyk_accepts({"a": ["A"], "b": ["B"]}, [("S", "A", "B")], "S", ["a", "b"]))
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"cyk_cnf_parser_d57 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
