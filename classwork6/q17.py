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
def is_even(n):
    if(n%2==0):
        return True
    else:
        return False
def main():
    iss = is_even(6)
    print(iss)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion