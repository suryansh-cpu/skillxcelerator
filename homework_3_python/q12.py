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
    {'name': 'John', 'age': 28},
    {'name': 'Anita', 'age': 35},
    {'name': 'Karan', 'age': 30}
    ]
    b=[]
    for i in patients:
        if(i['age']%2!=0):
            b.append(i['name'])
    print(b)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion