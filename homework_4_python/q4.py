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
    patients = [
    {"name": "Alice", "bp": 140, "sugar": 200},
    {"name": "Bob", "bp": 120, "sugar": 150},
    {"name": "Cara", "bp": 160, "sugar": 220}
    ]
    for i in patients:
        if(i["bp"]>130 and i["sugar"]>180):
            print(i["name"])
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion