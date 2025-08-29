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
def lo(s1,s2):
    n,m = len(s1),len(s2)
    dp = [[0] * (m+1) for i in range(n)]
    for i in range(n):
        for j in range(m):
            if(s1[i]==s2[j]):
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[n-1][m-1]
def main():
    s1 = "ABCDEFI"
    # s2 = "GCDHIE"
    s2 = "XYAEZF"
    ans=lo(s1,s2)
    print(ans)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion




def knapsack(n, W, weights, values):
    dp = [0] * (W + 1)

    for i in range(n):
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[W]


def knapsack(values, weights, W):
    n = len(values)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i-1] <= w:
                # Max of taking or not taking the item
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]
