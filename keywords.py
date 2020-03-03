# Shows Python's default keywords.

import keyword

for n, keyword in enumerate(keyword.kwlist):
    print(f"{n:2d}: {keyword}")