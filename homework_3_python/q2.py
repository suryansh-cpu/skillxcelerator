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
    match_scores = {'TeamA': 3, 'TeamB': 2, 'TeamC':5,'TeamD':8}
    winner = ''
    max =0
    for i in match_scores:
        # print(match_scores[i])
        if(match_scores[i]>max):
            max = match_scores[i]
            winner = i
    print(winner)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion