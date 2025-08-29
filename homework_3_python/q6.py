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
    runs, balls = 45,30
    ans = (runs / balls) * 100
    # print(round(ans,2))
    print(f"{ans:.2f}")
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion