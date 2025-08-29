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
# def queue_insert(a):
#     s.append(a)
# def s_out():

def main():
    queue=[1,2,3,4,5]
    s=[]
    n = len(queue)
    while queue:
        s.append(queue.pop(0))
        # queue.remove(i)
    while s:
        queue.append(s.pop())
        # s.pop()
    print(queue)
    pass
threading.Thread(target=main).start() #for increasing stack size for recurrsion