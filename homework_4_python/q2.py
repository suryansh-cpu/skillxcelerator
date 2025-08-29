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
    teams = ["Barcelona", "Juventus", "ParisSaintGermain", "Chelsea"]
    longest = 0
    vowel=0
    name = ""
    for i in teams:
        if(len(i) > longest):
            longest = len(i)
            name = i
    for i in name:
        if(i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'u' or i == 'U' or i == 'o' or i == 'O'):
            vowel+=1
    print(name)
    print(vowel)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion