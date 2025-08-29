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
    player_names = ['Messi', 'Neymar', 'Mbappe', 'Suarez']
    a=[]
    for i in player_names:
        if(len(i)>5):
            a.append(i)
    print(a)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion