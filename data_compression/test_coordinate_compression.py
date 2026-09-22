import doctest
import importlib.util
from pathlib import Path

_MODULE_PATH = Path(__file__).with_name("coordinate_compression.py")


def _load():
    spec = importlib.util.spec_from_file_location("coordinate_compression", _MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_doctests():
    module = _load()
    result = doctest.testmod(module)
    assert result.attempted > 0
    assert result.failed == 0
