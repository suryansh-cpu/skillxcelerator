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
#     l = []
#     s = str(input())
#     for i in s:
#         if(i == "{" or i == "[" or i == "("):
#             l.append(i)
#         else:
#             if((i==")" and l[-1:]=="(") or (i=="]" and l[-1:]=="[") or (i=="}" and l[-1:]=="{")):
#                 l.pop()
#             else:
#                 print("False")
#                 break
#     if(len(l)==0):
#         print("True")
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
    l = []
    s = str(input())
    iss = True
    for i in s:
        if i in "{[(":
            l.append(i)
        else:
            if not l:
                iss = False
                break
            if (i == ")" and l[-1] == "(") or (i == "]" and l[-1] == "[") or (i == "}" and l[-1] == "{"):
                l.pop()
            else:
                iss = False
                break
    if len(l) == 0 and iss:
        print("True")
    else:
        print("False")
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion