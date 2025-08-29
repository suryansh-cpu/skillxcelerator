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
    words = ["photosynthesis", "respiration", "chlorophyll", "transpiration"]
    best_word = ""
    count=0
    ctr = 0
    for j in words:
        dic={}
        for i in j:
            if i in dic.keys():
                dic[i]+=1
            else:
                dic[i]=1
        if(len(dic)>count):
            count = len(dic)
            best_word = j
    print(best_word)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion