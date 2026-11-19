from typing import Protocol

class AlgorithmContract(Protocol):
    def module_slug(self) -> str: ...

def contract_slug() -> str:
    return "stoer_wagner_mincut_py"
