import time
from core import RedBlackOrderedMap


def main() -> None:
    m = RedBlackOrderedMap()
    t0 = time.perf_counter_ns()
    for i in range(20_000):
        m.insert((i * 2654435761) & 0xFFFF, i)
    elapsed = (time.perf_counter_ns() - t0) / 1e6
    assert m.count > 10_000
    print(f"rbtree_ordered_map: {elapsed:.3f} ms nodes={m.count}")


if __name__ == "__main__":
    main()
