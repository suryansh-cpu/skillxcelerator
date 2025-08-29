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
    players = {
    "Messi": "PSG",
    "Ronaldo": "Al-Nassr",
    "Mbappe": "PSG"
    }
    dic={}
    for i in players:
        if players[i] not in dic.keys():
            dic[players[i]]=[]
        dic[players[i]].append(i)
    print(dic)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion