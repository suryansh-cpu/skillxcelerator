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
    input = [2, 5, 4, 6, 3]
    for i in input:
        if(i==6):
            print("6 found")
            break
        else:
            print(i)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion