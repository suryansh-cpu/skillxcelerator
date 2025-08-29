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
#     arr = []
#     new=[]
#     n = int(input())
#     for i in range(n):
#         a = int(input())
#         arr.append(a)
#     pointer = 1
#     for i in range(0,len(arr)):
#         if(pointer<=i or arr[pointer]<arr[i]):
#             while(arr[pointer]<arr[i] and pointer<len(arr)):
#                 pointer+=1
#         if(arr[pointer]>arr[i]):
#             new.append(arr[pointer])
#             pointer = (i+1)
#         else:
#             new.append(-1)
#             pointer = i+1
#     print(new)
#     pass
# threading.Thread(target=main).start() #for increasing stack size for recurrsion

# import sys
# import threading

# input = lambda: sys.stdin.readline().strip()
# print = lambda *args, **kwargs: __builtins__.print(*args, **kwargs, flush=True)

# def main():
#     arr = []
#     res = []
#     n = int(input())
#     for _ in range(n):
#         arr.append(int(input()))
    
#     for i in range(n):
#         next_greater = -1
#         for j in range(i + 1, n):
#             if arr[j] > arr[i]:
#                 next_greater = arr[j]
#                 break
#         res.append(next_greater)
    
#     print(res)

# threading.Thread(target=main).start()
import sys
import threading

input = lambda: sys.stdin.readline().strip()
print = lambda *args, **kwargs: __builtins__.print(*args, **kwargs, flush=True)

def main():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    res = [-1] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(arr[i])
    print(res)

threading.Thread(target=main).start()
