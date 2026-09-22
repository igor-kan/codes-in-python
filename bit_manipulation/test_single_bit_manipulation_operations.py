import doctest
import importlib.util
from pathlib import Path

_MODULE_PATH = Path(__file__).with_name("single_bit_manipulation_operations.py")


def _load():
    spec = importlib.util.spec_from_file_location("single_bit_manipulation_operations", _MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_doctests():
    module = _load()
    result = doctest.testmod(module)
    assert result.attempted > 0
    assert result.failed == 0
