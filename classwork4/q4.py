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
    lst = [1,2,3,4,5,6,7,8]
    n = len(lst)
    if(n%2 == 0):
        print(lst[0])
        print(lst[len(lst)-1])
        print(lst[(len(lst))//2])
        print(lst[(len(lst))//2 + 1])
    # first,last = lst[0],lst[n]
    # print(first)
    # print(last)
    # # print(middle)
    else:
        print(lst[0])
        print(lst[len(lst)-1])
        print(lst[(len(lst)-1)//2])
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion