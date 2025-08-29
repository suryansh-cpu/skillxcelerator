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
    lists = [[]*n]*n
    # lists=[]
    # print(len(lists))
    for i in range(n):
        for j in range(n):
            a = int(input())
            lists[i][j]=a
    print(lists)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion