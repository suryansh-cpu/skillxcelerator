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
    d = { "Mickey": 27, "Donald": 30 }
    rd = {}
    for i in d:
        rd[d[i]] = i
    print(rd)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion