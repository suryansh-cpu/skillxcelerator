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
    goals = {
    'Ronaldo': 9,
    'Messi': 13,
    'Neymar': 7,
    'Mbappe': 11
    }   
    top_3 = []

    for _ in range(3):
        max_player = None
        max_goals = -1

        for player, goal in goals.items():
            if player not in top_3 and goal > max_goals:
                max_goals = goal
                max_player = player

        top_3.append(max_player)

    print(top_3)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion