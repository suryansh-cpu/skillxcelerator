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
    mickey_info = {"age" : 12,"pet":("Pluto"),"hobbies":["magic", "dancing"]}
    print(mickey_info)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion