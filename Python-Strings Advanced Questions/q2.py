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
    input = ["abc", "bcd", "cde"]
    a = input[0]
    for i in range(1,len(input)):
        # j = i[]
        loca = 0
        k=input[i[0]]
        for loc,j in enumerate(a):
            if(j == k):
                loca = loc
        for j in range(loca,len(a)):
            
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion