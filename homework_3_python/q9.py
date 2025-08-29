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
    match = {'TeamA': 2, 'TeamB': 2}
    max=0
    min=1212121
    for i in match:
        # if(max == match[i]):
        #     print("Extra Time")
        #     pass
        if(match[i]>max):
            max = match[i]
        if(match[i]<min):
            min = match[i]
    if(max == min):
        print("Extra Time")
    else:
        print(max - min)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion