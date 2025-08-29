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
    s = s.replace('.',' ')
    word = s.split()
    dic = {}
    # s.split()
    for i in word:
        dic[i] = dic.get(i, 0) + 1
    sorted_desc = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True)) # saw from chatgpt
    # print(sorted_des)
    first_key = next(iter(sorted_desc)) # chatgpt
    print(first_key)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion