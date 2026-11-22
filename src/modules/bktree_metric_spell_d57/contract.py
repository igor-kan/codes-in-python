from typing import Protocol

class AlgorithmContract(Protocol):
    def module_slug(self) -> str: ...

def contract_slug() -> str:
    return "bktree_metric_spell_d57"
