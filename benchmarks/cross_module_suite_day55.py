#!/usr/bin/env python3
"""Cross-module verification & benchmark runner for all Day 55 `codes-in-python` modules."""

import importlib.util
import pathlib
import sys
import time

SLUGS = ['stoer_wagner_mincut_py', 'johnsons_apsp_heapq_py', 'hungarian_assign_o_n3_py', 'suffix_automaton_dawg_py', 'eertree_palin_tree_py']


def main() -> None:
    root = pathlib.Path(__file__).resolve().parent.parent / "src" / "modules"
    total = 0
    t0 = time.perf_counter_ns()
    for slug in SLUGS:
        mod_dir = root / slug
        sys.path.insert(0, str(mod_dir))
        try:
            spec = importlib.util.spec_from_file_location(f"{slug}_fast", mod_dir / "fast_path.py")
            mod = importlib.util.module_from_spec(spec)
            assert spec.loader is not None
            spec.loader.exec_module(mod)
            total ^= mod.fast_fold_ints([1, 2, 3, 4])
        finally:
            sys.path.pop(0)
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"codes-in-python day55 suite ok modules={len(SLUGS)} ms={ms:.3f} fold={total}")


if __name__ == "__main__":
    main()
