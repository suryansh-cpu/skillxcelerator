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
    jerseys = [7, 10, 11, 14, 23, 30, 33]
    search = 23
    low = 0
    high = len(jerseys) - 1
    found = False
    while low <= high:
        mid = (low + high) // 2
        if jerseys[mid] == search:
            print("Found at index:", mid)
            found = True
            break
        elif jerseys[mid] < search:
            low = mid + 1
        else:
            high = mid - 1
    if not found:
        print("Jersey not found")
threading.Thread(target=main).start()
