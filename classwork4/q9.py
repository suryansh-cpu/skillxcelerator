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
    lst = ['amazon','google','apple']
    print(lst[0])
    print(lst[len(lst)-1])
    print(lst[(len(lst)-1)//2])
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion