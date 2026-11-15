import time
from fast_path import decode_states_fast
from models import HmmParameters


def main() -> None:
    params = HmmParameters(
        initial_probs=(0.5, 0.3, 0.2),
        transition_matrix=((0.6, 0.3, 0.1), (0.2, 0.6, 0.2), (0.1, 0.3, 0.6)),
        emission_matrix=((0.7, 0.2, 0.1), (0.2, 0.6, 0.2), (0.1, 0.2, 0.7)),
    )
    obs = [i % 3 for i in range(4000)]
    t0 = time.perf_counter_ns()
    path = decode_states_fast(params, obs)
    elapsed_ms = (time.perf_counter_ns() - t0) / 1e6
    assert len(path) == 4000
    print(f"viterbi_hmm_decoder: {elapsed_ms:.3f} ms len={len(path)}")


if __name__ == "__main__":
    main()
