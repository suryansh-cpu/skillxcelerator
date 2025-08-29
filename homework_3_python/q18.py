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
    players = {'Rahul': 75, 'Kohli': 102, 'Rohit': 120}
    b=[]
    for i in players:
        if players[i] > 100:
            b.append(i)
    print(b)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion