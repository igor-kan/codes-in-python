from typing import Dict, List, Protocol, Tuple

class CfgRecognizer(Protocol):
    def recognizes(self, tokens: List[str]) -> bool: ...
