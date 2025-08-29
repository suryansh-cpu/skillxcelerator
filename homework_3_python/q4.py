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
    patients = {'John': 98.6, 'Priya': 101.4, 'Ali': 99.0, 'Neha': 103.5}
    ans = []
    for i in patients:
        if(patients[i]>=100.0):
            ans.append(i)
    print(ans)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion