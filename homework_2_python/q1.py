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
    if(len(s)<2):
        print(s)
    else:
        s = list(s)
        a = s[0]
        s[0] = s[len(s)-1]
        s[len(s)-1] = a
        # print(s)
        print(''.join(s))
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion