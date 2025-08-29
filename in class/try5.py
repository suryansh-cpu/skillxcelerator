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
    b=str(input())
    # b.split(' ')
    c=[]
    for i in b:
        # a = int(input())
        if( i!=0 ):
            c.append(i)
    c.extend(['0']*(n - len(b)))
    print(str(c))
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion