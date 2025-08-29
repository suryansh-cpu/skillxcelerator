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
#     n = int(input())
#     i = 1
#     while(i*i < n):
#         i+=1
#     if(i*i == n):
#         print(i)
#     else:
#         print(f"No perfect square root found but lies around {i-1} to {i+1}")
#     pass

# threading.Thread(target=main).start() #for increasing stack size for recurrsion

#****************** approach 2 ******************
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
    n = int(input())
    p1,p2,p3 = 2,100,50
    while(p3*p3 != n):
        if(p3*p3>n):
            p2 = p3
            p3 = (p2+p1)//2
        elif(p3*p3<n):
            p1 = p3
            p3 = (p1+p2)//2
    print(p3)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion