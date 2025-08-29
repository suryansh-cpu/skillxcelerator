import sys
import math
import bisect
import heapq
import itertools
import collections
import functools
import operator
import threading
from collections import Counter
input = lambda: sys.stdin.readline().strip()
print = lambda *args, **kwargs: __builtins__.print(*args, **kwargs, flush=True)

def main():
    n = int(input())
    lst = input()
    # for _ in range(n):
    #     lst = input()
    frequency_counter = Counter(lst.split())
    print(frequency_counter)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion