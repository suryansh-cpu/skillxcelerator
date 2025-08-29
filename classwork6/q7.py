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
    backpack = ["Water", "Map", "Snacks"]
    for i,item in enumerate(backpack):
        print(f"{i+1}. {item}")
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion