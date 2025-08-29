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
    friends_ages = {"Mickey":20,"minnie":18,"donald":33}
    friends_ages["Pluto"] = 5
    friends_ages["minnie"]=29
    for i in friends_ages:
        print(f"{i} is {friends_ages[i]} years old")
    # print(friends_ages)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion