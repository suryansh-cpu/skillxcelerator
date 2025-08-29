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
    s = str(input())
    dic = {'a' : 0,'A' : 0,'e' : 0,'E' : 0,'i':0,'I':0,'O':0,'o':0,'u':0,'U':0}
    for i in s:
        if i in dic:
            dic[i]+=1
    print(dic)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion