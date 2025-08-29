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
    tokens = ["2", "1", "+", "3", "*","4","/"]
    a,b = 0,0
    for i in tokens:
        if(i == "*"):
            a = int(a)*int(b)
            b=0
        elif(i=="/"):
            a = int(a)/int(b)
            b=0
        elif(i=="+"):
            a = int(a)+int(b)
            b=0
        elif(i=="-"):
            a = abs(int(a)-int(b))
            b=0
        else:
            if(a==0):
                a = i
            else:
                b = i
    print(a)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion