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
l = []
def ins(a):
    l.append(a)
def rem():
    l.pop()
def peek():
    return l[-1:]
def main():
    ins(10)
    ins(20)
    ins(30)
    rem()
    print(peek())
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion