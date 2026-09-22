import runpy
from pathlib import Path

_MODULE = Path(__file__).with_name("stack_min.py")


def test_main_asserts():
    runpy.run_path(str(_MODULE), run_name="__main__")
