import time
from core import DinicMaxFlowSolver
from models import DirectedCapEdge


def main() -> None:
    edges = [DirectedCapEdge(i, i + 1, 100) for i in range(99)]
    edges.extend(DirectedCapEdge(i, min(99, i + 7), 15) for i in range(92))
    t0 = time.perf_counter_ns()
    rep = DinicMaxFlowSolver().solve(100, edges, 0, 99)
    elapsed = (time.perf_counter_ns() - t0) / 1e6
    assert rep.max_flow > 0
    print(f"ford_fulkerson_scaling: {elapsed:.3f} ms flow={rep.max_flow}")


if __name__ == "__main__":
    main()
