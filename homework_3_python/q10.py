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
    players = ['Virat Kohli', 'MS Dhoni', 'Rohit Sharma']
    a = []
    for i in players:
        b = i.split()
        a.append(b[1][0])
    print(a)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion