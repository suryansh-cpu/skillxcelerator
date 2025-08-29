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
    it_companies = ['amazon','google','apple','IBM']
    n = len(it_companies)
    if(n%2==0):
        middle = n//2
        del(it_companies[middle])
        del(it_companies[middle-1])
    else:
        middle = n//2
        del(it_companies[middle])
    print(it_companies)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion