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
    input = "experiment successful theory failed"
    a = input.split()
    for i in range(len(a)):
        # i=i[::-1]
        a[i] = a[i][::-1]
    b=""
    for i in a:
        b+=i
        b+=" "
    print(b)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion