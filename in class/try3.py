# import sys
# import math
# import bisect
# import heapq
# import itertools
# import collections
# import functools
# import operator
# import threading

# input = lambda: sys.stdin.readline().strip()
# print = lambda *args, **kwargs: __builtins__.print(*args, **kwargs, flush=True)

# def main():
#     # l1 = input()
#     l1 = list(map(int, input().split()))
#     sum = int(input())
#     l2 = []
#     l3 = []
#     for i in l1:
#         if(not((sum - i) in l2)):
#             l2.append(i)
#             # l2.append(sum - i)
#         elif ((sum - i) in l2):
#             l3.append(i)
#             l3.append(sum - i)
#             print(l3)
#             break
#     # print(lst)
#     pass

# threading.Thread(target=main).start() #for increasing stack size for recurrsion
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
    l1 = list(map(int, input().split()))
    sum = int(input())
    p2 = len(l1)-1
    p1 = 0
    while(l1[p1]+l1[p2] != sum):
        if(l1[p1]+l1[p2]>sum):
            p2-=1
        elif (l1[p1]+l1[p2]<sum):
            p1-=1
    print(l1[p1])
    print(l1[p2])
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion