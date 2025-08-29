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
    friends_ages = {"Mickey":20,"minnie":18,"donald":33,"goofy":22}
    friends_ages["Pluto"] = 5
    print(friends_ages["donald"])
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion