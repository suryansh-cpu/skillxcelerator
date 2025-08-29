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
def lo(s1, s2):
    n, m = len(s1), len(s2)
    dpc = [0] * (m)
    # dpc = [0] * (m)
    # max_len = 0
    # end_idx = 0
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                dpc[j]=1
                break
        #         if i > 0 and j > 0:
        #             dpc[j] = dpp[j - 1] + 1
        #         else:
        #             dpc[j] = 1
        #         if dpc[j] > max_len:
        #             max_len = dpc[j]
        #             end_idx = i + 1
        #         break
        #     else:
        #         dpc[j] = 0
        # dpp, dpc = dpc, [0]*m
    #     print("Max length is : ",max_len)
    # print("Max length is : ",max_len)
    # return s1[end_idx - max_len:end_idx]
    # print(dpc)
    s=""
    for i in range(len(dpc)):
        if(dpc[i]==1):
            s=s+s2[i]
    print(s)
    return sum(dpc)
def main():
    # longest common subsequence...............
    s1 = "ABCDEF"
    # s2 = "GCDHIE"
    s2 = "GCDECDEF"
    ans=lo(s1,s2)
    print(ans)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion