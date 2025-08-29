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
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
    front_end.extend(back_end)
    full_stack = front_end
    n = len(full_stack)
    # print(full_stack)
    for i in range(0,n,1):
        if(full_stack[i] == 'Redux'):
            full_stack.insert(i+1,'Python')
            full_stack.insert(i+2,'SQL')
    print(full_stack)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion