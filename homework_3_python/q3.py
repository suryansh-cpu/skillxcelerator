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
    text = "The mitochondria is the powerhouse of the cell"
    a = text.split()
    iss = False
    for i in a:
        if(iss):
            print(i)
            iss = False
            # break
        if(i == "is"):
            iss = True
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion