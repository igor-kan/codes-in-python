from typing import Dict, List
from models import Suggestion


def verify_top_k(model: Dict[str, int], prefix: str, k: int, got: List[Suggestion]) -> None:
    expected = sorted(
        ((w, sc) for w, sc in model.items() if w.startswith(prefix)),
        key=lambda item: (-item[1], item[0]),
    )[:k]
    assert [(s.term, s.score) for s in got] == expected
