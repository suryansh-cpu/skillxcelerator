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
    n = int(input())
    sum=0
    for i in range(1,n+1):
        sum+=i
    print(sum)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion