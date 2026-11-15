import unittest
from core import LogSpaceHmmDecoder
from fast_path import decode_states_fast
from invariants import verify_viterbi_optimality
from models import HmmParameters
from validation import validate_hmm


class TestViterbiHmm(unittest.TestCase):
    def test_rainy_sunny_decode(self) -> None:
        params = HmmParameters(
            initial_probs=(0.6, 0.4),
            transition_matrix=((0.7, 0.3), (0.4, 0.6)),
            emission_matrix=((0.5, 0.4, 0.1), (0.1, 0.3, 0.6)),
        )
        obs = (0, 1, 2)
        validate_hmm(params, obs)
        res = LogSpaceHmmDecoder().decode(params, obs)
        verify_viterbi_optimality(params, obs, res)
        self.assertEqual(res.states, (0, 0, 1))
        self.assertEqual(list(res.states), decode_states_fast(params, obs))


if __name__ == "__main__":
    unittest.main()
