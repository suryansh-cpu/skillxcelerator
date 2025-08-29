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
# q = []
s1 = []
s2 = []
def enqueue(a):
    s1.append(a)
def dequeue():
    if(len(s2)==0):
        for i in range(len(s1)):
            s2.append(s1.pop())
    if not s2:
        print("Queue is empty")
        return None
    return s2.pop()
def main():
    enqueue(1)
    enqueue(2)
    enqueue(3)
    # enqueue(90)
    print(dequeue())
    print(dequeue())
    print(dequeue())
    print(dequeue())
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion