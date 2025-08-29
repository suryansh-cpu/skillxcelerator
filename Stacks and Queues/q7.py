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
    nums = []
    n = int(input())
    k = int(input())
    for _ in range(n):
        a = int(input())
        nums.append(a)
    ans=[]
    for i in range(0,n-k,1):
        
    # for i in range(0,n-2):
    #     a = nums[i]
    #     b = nums[i+1]
    #     c = nums[i+2]
    #     ans.append(max(max(a,b),c))
    print(ans)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion