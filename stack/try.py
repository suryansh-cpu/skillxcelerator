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
# st_size=12
st = []
def check(a):
    if (a == '[' or a == '(' or a == '{'):
        return True
    else:
        return False
def add(a):
    # if(is_full()):
    #     print("Stack is full cannot insert")
    # else:
    #     # print(f"inserted {a}")
        st.append(a)
def remove():
    if(is_empty()):
        print("Already empty")
    else:
        # print(f"removed last element {st[-1]}")
        st.pop()
def see():
    if(is_empty()):
        return "-1"
    else:
        # print(st[-1])
        return (st[-1])
def is_empty():
    if(len(st)==0):
        return True
    else:
        return False
# def is_full():
#     if(len(st)==12):
#         return True
#     else:
#         return False
def display():
    if(not is_empty()):
        print("invalid string")
    else:
        print("valid string")
def main():
    # a = st
    s = (input())
    add(s[0])
    max=0
    count=0
    for i in range(1,len(s)):
        if(check(s[i])):
            add(s[i])
        elif(not check(s[i])):
            b=see()
            if(b=="-1"):
                if(max<count):
                    max=count
                    count=0
                add(s[i])
                # break
            elif((s[i]==']' and b == '[') or (s[i]==')' and b == '(') or (s[i]=='}' and b == '{')):
                count+=2
                if(max<count):
                    max=count
                remove()
            else:
                # break
                if(max<count):
                    max=count
                count=0
    print(max)
    # print(1)
    display()
    pass

threading.Thread(target=main).start() #for increasing st size for recurrsion

# import sys
# import threading

# input = lambda: sys.stdin.readline().strip()
# print = lambda *args, **kwargs: __builtins__.print(*args, **kwargs, flush=True)

# st = []

# def check(a):
#     if a == '[' or a == '(' or a == '{':
#         return True
#     else:
#         return False

# def add(a):
#     st.append(a)

# def remove():
#     if is_empty():
#         print("Already empty")
#     else:
#         st.pop()

# def see():
#     if is_empty():
#         return "-1"
#     else:
#         return st[-1]

# def is_empty():
#     return len(st) == 0

# def display():
#     if not is_empty():
#         print("invalid string")
#     else:
#         print("valid string")

# def main():
#     s = input()
#     max_count = 0
#     count = 0
#     # st.clear()

#     for i in range(len(s)):
#         if check(s[i]):
#             add(s[i])
#         else:
#             b = see()
#             if b == "-1":
#                 count = 0
#             elif (s[i] == ']' and b == '[') or (s[i] == ')' and b == '(') or (s[i] == '}' and b == '{'):
#                 remove()
#                 count += 2
#                 if count > max_count:
#                     max_count = count
#             else:
#                 count = 0
#                 # st.clear()

#     print(max_count)
#     display()

# threading.Thread(target=main).start()
