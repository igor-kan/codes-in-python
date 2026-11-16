from concurrent.futures import ThreadPoolExecutor
from typing import List, Sequence
from core import CooleyTukeyFFT
from models import SpectrumResult


def batch_forward_fft(signals: Sequence[Sequence[complex]]) -> List[SpectrumResult]:
    eng = CooleyTukeyFFT()
    with ThreadPoolExecutor(max_workers=4) as pool:
        return list(pool.map(eng.forward, signals))
