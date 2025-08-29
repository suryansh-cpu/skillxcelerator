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
    # if "daisy" in friends_ages:
    #     print("She is in the castle")
    # else:
    #     print("Not in the castle")
    # pass
    friends_ages["Daisy"] = 25
    party_guests = friends_ages.copy()
    print(party_guests)
threading.Thread(target=main).start() #for increasing stack size for recurrsion