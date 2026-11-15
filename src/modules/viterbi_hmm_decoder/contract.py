from typing import Protocol, Sequence
from models import HmmParameters, ViterbiResult


class SequenceDecoderProtocol(Protocol):
    def decode(self, params: HmmParameters, observations: Sequence[int]) -> ViterbiResult:
        ...
