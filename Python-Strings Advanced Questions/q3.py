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
    print("Enter pattern :")
    s = str(input())
    a = str(input())
    a.split(" ")
    n = len(s)
    j = n-1
    is_true = True
    for i in range(0,(n//2)-1):
        if(s[i]!=s[j]):
            print("NO")
            is_true = False
            break
        else:
            i+=1
            j-=1
    if(is_true):
        print("Yes")
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion