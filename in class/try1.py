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
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    l3 = []
    for i in l2:
        if i in l1:
            l3.append(i)
    l3.sort(reverse=True)
    unique = list(set(l3))
    print(unique)
    # print(l3.sort(reverse = True))
    # print(l1)
    # print(l2)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion