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
#     s1 = [34, 3, 31, 98, 92, 23]
#     s2 = []
#     for i in range(len(s1)):
#         s3 = s1.pop()
#         while s1 and s1[-1] > s3:
#             s2.append(s1.pop())
#         s2.append(s3)
#     while s2:
#         s1.append(s2.pop())
#     print(s1)
#     pass

# threading.Thread(target=main).start() #for increasing stack size for recurrsion
def sort_stack(input_stack):
    temp_stack = []
    while input_stack:
        temp = input_stack.pop()
        while temp_stack and temp_stack[-1] > temp:
            input_stack.append(temp_stack.pop())
        temp_stack.append(temp)
    while temp_stack:
        input_stack.append(temp_stack.pop())

    return input_stack
if __name__ == "__main__":
    stack = [34, 3, 31, 98, 92, 23]
    print(stack[::-1])

    sorted_stack = sort_stack(stack)

    print(sorted_stack[::-1])
