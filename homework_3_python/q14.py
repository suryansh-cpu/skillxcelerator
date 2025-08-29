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
    scores = {
    'Gill': 52,
    'Kohli': 90,
    'Dhawan': 38,
    'Pant': 64
    }
    b=[]
    for i in scores:
        if(scores[i]>=50):
            b.append(i)
    print(b)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion