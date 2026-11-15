import time
from fast_path import flat_astar_distance
from models import GridMap


def main() -> None:
    walls = frozenset((i, 25) for i in range(48))
    grid = GridMap(rows=50, cols=50, blocked=walls)
    t0 = time.perf_counter_ns()
    d = flat_astar_distance(grid, (0, 0), (0, 49))
    elapsed = (time.perf_counter_ns() - t0) / 1e6
    assert d > 0
    print(f"a_star_priority_router: {elapsed:.3f} ms dist={d}")


if __name__ == "__main__":
    main()
