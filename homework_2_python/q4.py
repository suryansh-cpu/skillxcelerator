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
    neww = s[0]
    ss = ' '
    n = len(s)
    count=1
    for i in range(1,n,1):
        if(s[i] == neww):
            count+=1
        elif count>1:
            ss+=neww
            ss+=str(count)
            count = 1
            neww = s[i]
        else:
            ss+=neww
            neww = s[i]
    ss += neww
    if count > 1:
        ss += str(count)
    print(ss)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion