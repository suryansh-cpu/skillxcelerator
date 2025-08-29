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
    players = [
        {"name": "Kohli", "scores": [54, 76, 102, 90]},
        {"name": "Rohit", "scores": [45, 88, 60, 40]},
        {"name": "Gill", "scores": [70, 80, 77, 120]}
    ]

    ans = {}
    for player in players:
        scores = player["scores"]
        avg = sum(scores) / len(scores)
        ans[player["name"]] = avg

    print(ans)

threading.Thread(target=main).start() #for increasing stack size for recurrsion