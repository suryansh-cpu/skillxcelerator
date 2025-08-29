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
    it_companies = ['amazon','google','apple','IBM']
    mid = len(it_companies) // 2
    it_companies = it_companies[:mid] + it_companies[mid+1:]
    print(it_companies)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion

# Q21 Q21 Q21 Q21

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
    it_companies = ['amazon','google','apple','IBM']
    del(it_companies[0])
    print(it_companies)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion

# Q22 Q22 Q22 Q22

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
    it_companies = ['amazon','google','apple','IBM']
    n = len(it_companies)
    if(n%2==0):
        middle = n//2
        del(it_companies[middle])
        del(it_companies[middle-1])
    else:
        middle = n//2
        del(it_companies[middle])
    print(it_companies)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion

#Q23 Q23 Q23 Q23

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
    it_companies = ['amazon','google','apple','IBM']
    n = len(it_companies)
    del(it_companies[n-1])
    print(it_companies)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion

#Q24 Q24 Q24 Q24 Q24

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
    it_companies = ['amazon','google','apple','IBM']
    it_companies.clear()
    print(it_companies)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion

#Q25 Q25 Q25 Q25

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
    it_companies = ['amazon','google','apple','IBM']
    del(it_companies)
    # print(it_companies)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion

#Q26 Q26 Q26 Q26

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
    print(front_end)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion

#Q27 Q27 Q27 Q27

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
    print(full_stack)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion


#Q28 Q28 Q28 Q28

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