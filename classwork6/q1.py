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
    toppings = ["Cheese", "Tomato", "Pepperoni", "Mushroom"]
    for i in toppings:
        print(i)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion