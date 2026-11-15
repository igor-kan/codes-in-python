import random
import unittest
from core import LogSpaceHmmDecoder
from invariants import verify_viterbi_optimality
from models import HmmParameters
from validation import validate_hmm


class TestViterbiProperties(unittest.TestCase):
    def test_random_hmms_brute_match(self) -> None:
        rng = random.Random(2026)
        dec = LogSpaceHmmDecoder()
        for _ in range(15):
            r1 = rng.random() + 0.1
            r2 = rng.random() + 0.1
            init = (r1 / (r1 + r2), r2 / (r1 + r2))
            t0 = rng.random() + 0.1
            t1 = rng.random() + 0.1
            t2 = rng.random() + 0.1
            t3 = rng.random() + 0.1
            trans = ((t0 / (t0 + t1), t1 / (t0 + t1)), (t2 / (t2 + t3), t3 / (t2 + t3)))
            e0 = rng.random() + 0.1
            e1 = rng.random() + 0.1
            e2 = rng.random() + 0.1
            e3 = rng.random() + 0.1
            emit = ((e0 / (e0 + e1), e1 / (e0 + e1)), (e2 / (e2 + e3), e3 / (e2 + e3)))
            params = HmmParameters(init, trans, emit)
            obs = tuple(rng.randrange(2) for _ in range(5))
            validate_hmm(params, obs)
            res = dec.decode(params, obs)
            verify_viterbi_optimality(params, obs, res)


if __name__ == "__main__":
    unittest.main()
