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
    data = "covid19spread2023"
    dic = {}
    for i in data:
        if(i>='a' and i<='z'):
            if i in dic.keys():
                dic[i]+=1
            else:
                dic[i]=1
    largest = 0
    charr = ""
    for i in dic:
        # print(i)
        if(dic[i]>largest):
            largest = dic[i]
            charr = i
    print(charr)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion