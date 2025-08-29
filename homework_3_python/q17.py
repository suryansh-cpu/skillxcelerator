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
    goals = [0, 1, 2, 0, 3, 2]
    cnt = 0
    sum=0
    for i in goals:
        if(cnt%2==0):
            sum+=i
        cnt+=1
    print(sum)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion