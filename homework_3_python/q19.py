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
    a = "Einstein had a creative mind"
    b = ['a','e','i','o','u','A','E','I','O','U']
    c=0
    for i in a:
        if (i in b):
            c+=1
    print(c)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion