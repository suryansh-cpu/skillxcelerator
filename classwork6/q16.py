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
def fact(n):
    num = 1
    while(n>0):
        num *= n
        n-=1
    print(num)
def main():
    fact(5)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion