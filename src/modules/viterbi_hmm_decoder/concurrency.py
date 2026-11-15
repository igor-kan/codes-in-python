from concurrent.futures import ThreadPoolExecutor
from typing import List, Sequence
from core import LogSpaceHmmDecoder
from models import HmmParameters, ViterbiResult


def batch_decode_sequences(
    params: HmmParameters, sequences: Sequence[Sequence[int]], workers: int = 2
) -> List[ViterbiResult]:
    decoder = LogSpaceHmmDecoder()
    with ThreadPoolExecutor(max_workers=workers) as pool:
        return list(pool.map(lambda seq: decoder.decode(params, seq), sequences))
