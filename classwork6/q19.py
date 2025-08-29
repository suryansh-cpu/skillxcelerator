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
def summ(s):
    a=0
    for i in s:
        a+=i
    print(a)
def main():
    summ([1, 2, 3, 4, 5])
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion