# Shows built-in and installed modules.

import pkgutil

modules = pkgutil.iter_modules()

for n, module in enumerate(modules):
    print(f"{n:2d}: {module.name}")