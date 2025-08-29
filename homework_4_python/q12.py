import sys
import math
import bisect
import heapq
import itertools
import collections
import functools
import operator
import threading

input = lambda: sys.stdin.readline().strip()
print = lambda *args, **kwargs: __builtins__.print(*args, **kwargs, flush=True)

def main():
    text = "Photosynthesis happens in chlorophyll using sunlight"
    definitions = {
        "Photosynthesis": "a process in plants",
        "chlorophyll": "a green pigment"
    }
    for term, definition in definitions.items():
        text = text.replace(term, definition)
    print(text)
    pass
threading.Thread(target=main).start() #for increasing stack size for recurrsion