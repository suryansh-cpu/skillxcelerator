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
    players = [('Kohli', 18), ('Dhoni', 7), ('Rohit', 45), ('Pant', 17)]
    for i in players:
        # print(i)
        # print(i[0])
        if(i[1]%3==0):
            print(i[0])
        # print(players[i])
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion