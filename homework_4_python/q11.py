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
    stats = {
    "Kohli": [60, 70, 100],
    "Gill": [80, 90, 85],
    "Rohit": [30, 40, 50]
    }
    totals = {player: sum(runs) for player, runs in stats.items()}
    top_2 = sorted(totals.items(), key=lambda x: x[1], reverse=True)[:2]
    top_names = [player for player, _ in top_2]
    print("Top 2:", top_names)
    pass
threading.Thread(target=main).start() #for increasing stack size for recurrsion