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
    coins = [1, 2, 5]
    amount = 11
    dp=[1000]*(amount+1)
    dp[0]=0
    for coin in coins:
        for i in range(coin,amount+1):
            dp[i] = min(dp[i],dp[i-coin]+1)
    print(dp[amount])
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion