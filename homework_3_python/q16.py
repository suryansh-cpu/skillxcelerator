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
    {'name': 'Ankit', 'height': 1.7, 'weight': 70},
    {'name': 'Neha', 'height': 1.6, 'weight': 55}
    ]
    a=[]
    # BMI = weight / (height ** 2)
    for i in patients:
        BMI = i['weight'] / (i['height'] ** 2)
        if(BMI>24):
            a.append(i['name'])
    print(a)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion