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
    d={'vowel':0,'consonent':0}
    for i in s:
        if(i == 'a' or i=='e' or i=='i' or i=='o' or i=='u'):
            d['vowel']+=1
        else:
            d['consonent']+=1
    print(d)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion