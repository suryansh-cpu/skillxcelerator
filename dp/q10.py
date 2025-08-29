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
    a = [10, 9, 2, 5, 3, 7, 101, 18]
    # a = [1,3,6,4,5,7]
    # a = [1,2,3,-1,2]
    n = len(a)
    dp = [1]*n
    for i in range(n):
        for j in range(i):
            if(a[j]<a[i]):
                dp[i] = max(dp[i],dp[j]+1)
    print(max(dp))
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion
# 1,3,5,4,7