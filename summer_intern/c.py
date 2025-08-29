# import sys
# import math
# import bisect
# import heapq
# import itertools
# import collections
# import functools
# import operator
# import threading

# input = lambda: sys.stdin.readline().strip()
# print = lambda *args, **kwargs: __builtins__.print(*args, **kwargs, flush=True)
# def knap(n,i_value,i_weight,max_allowed):
#     dp = [[0] * (max_allowed + 1) for _ in range(n + 1)]
#     for i in range(1, n + 1):
#         for w in range(max_allowed + 1):
#             if i_weight[i-1] <= w:
#                 dp[i][w] = max(dp[i-1][w], i_value[i-1] + dp[i-1][w - i_weight[i-1]])
#             else:
#                 dp[i][w] = dp[i-1][w]

#     return dp[n][max_allowed]
# def main():
#     # knapsack problem........
#     n = int(input())
#     value=[]
#     weight=[]
#     max_allowed = int(input())
#     # max_allowed=int(input())
#     for _ in range(n):
#         a = int(input())
#         value.append(a)
#     for _ in range(n):
#         a = int(input())
#         weight.append(a)
#     ans = knap(n,value,weight,max_allowed)
#     print(ans)
#     pass

# threading.Thread(target=main).start() #for increasing stack size for recurrsion


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
def knap(n,i_value,i_weight,w):
    dp = [[0] * (w + 1) for _ in range(n + 1)]
    for i in range(1,n+1):
        for j in range(1,w+1):
            if(i_weight[i-1]<=w):
                dp[i][w]=max(dp[i-1][w],(i_value[i-1]+dp[i-1][w-i_weight[i-1]]))
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][w]
def main():
    n = int(input())
    value=[]
    weight=[]
    max_allowed = int(input())
    # max_allowed=int(input())
    for _ in range(n):
        a = int(input())
        value.append(a)
    for _ in range(n):
        a = int(input())
        weight.append(a)
    ans = knap(n,value,weight,max_allowed)
    print(ans)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion