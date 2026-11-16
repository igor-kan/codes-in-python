from core import KdTreeIndex
from invariants import verify_knn_oracle


def run_tests() -> None:
    pts = [(2.0, 3.0), (5.0, 4.0), (9.0, 6.0), (4.0, 7.0), (8.0, 1.0), (7.0, 2.0)]
    kd = KdTreeIndex(pts)
    verify_knn_oracle(kd, pts, (6.0, 3.0), 3)
    assert kd.range_box((4.0, 2.0), (8.0, 7.0)) == [1, 3, 5]


if __name__ == "__main__":
    run_tests()
