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
a = []
head=-1
tail=-1
def ins(b):
    global head, tail, a
    if(head==-1):
        head+=1
        tail+=1
        a.append(b)
    else:
        a.append(b)
        tail+=1
def rem():
    global head
    if(is_empty()):
        print("queue is empty,remove function cannot be processed")
    else:
        # a.remove(head)
        head+=1
def is_empty():
    global head, tail
    if(head>tail or head == -1):
        return True
    else:
        return False
def display():
    global head, tail, a
    print(a[head:tail+1])
def main():
    ins(1)
    ins(2)
    ins(3)
    display()
    rem()
    rem()
    ins(4)
    ins(5)
    rem()
    display()
    rem()
    rem()
    rem()
    display()
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion