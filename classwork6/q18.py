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
def reverse_string(s):
    print(s[::-1])
def main():
    reverse_string("python")
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion