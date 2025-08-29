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
    n=int(input())
    # num=0
    while(1):
        num = int(input())
        if(num==n):
            print("Correct!")
            break
        else:
            continue

    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion