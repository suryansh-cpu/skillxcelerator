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
def make_icecream(flavor, scoops):
    print(f"Making {scoops} scoops of {flavor} icecream")
def main():
    make_icecream("chocolate",2)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion