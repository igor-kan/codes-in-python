from typing import Protocol

class AlgorithmContract(Protocol):
    def module_slug(self) -> str: ...

def contract_slug() -> str:
    return "vose_alias_categorical_py"
