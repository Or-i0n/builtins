#! /usr/bin/python3

import builtins
from types import BuiltinFunctionType as BFT


def get_funcs():
    """Yields built-in funtion names."""

    for name, obj in vars(builtins).items():
        if isinstance(obj, BFT):
            yield name


for n, funcs in enumerate(get_funcs(), start=1):
    print(f"{n:2d}: {funcs}")
