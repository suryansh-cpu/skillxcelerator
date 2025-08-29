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
    num=10
    while(num>0):
        print(num)
        num-=1
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion