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
#     s = str(input())
#     n = len(s)
#     a = list(s)
#     for i in range(n-1,-1,-1):
#         if(a[i]!=']'):
#             break
#     for i in range(0,n-1,1):
#         if(a[i] == '['):
#             a[i] = '*'
#     print(a)
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
    # s = list(input())
    s = list(map(int, input().split()))
    freq = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,0:0}
    for i in s:
        freq[i]+=1
    highest = 0
    second = 0
    for i in range(0,9):
        if(freq[i]>highest):
            second = highest
            highest = freq[i]
        elif(freq[i]<highest and freq[i]>second):
            second = freq[i]
    # print(freq)
    print(second)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion