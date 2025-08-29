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
    input = "biology"
    b=[]
    for i in input:
        if(ord(i)%2==0):
            b.append(i)
    print(b)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion