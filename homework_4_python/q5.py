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
    goals = [2, 5, 8, 12, 13, 18, 20]
    search_goal = 10
    i,k = 0,len(goals)-1
    j = int(len(goals)//2)
    index = 0
    # print(i)
    # print(j,k)
    s=1
    while(s>0):
        if(search_goal==goals[j]):
            index = j
            break
        elif(search_goal<goals[j]):
            k = j
            j = (i+k)//2
        elif(search_goal>goals[j]):
            i = j
            j = (i+k)//2
        if(i == j or j == k):
            if(goals[j]!=search_goal):
                print("NO")
                break
    print(index)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion