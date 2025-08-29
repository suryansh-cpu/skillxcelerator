# ********************************** q20


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
#     patients = ['Amit', 'Neha', 'John', 'Sara']
#     rooms=[]
#     num=0
#     for i in patients:
#         rooms.append(f'Room-{num+1}: {i}')
#         num+=1
#     print(rooms)
#     pass

# threading.Thread(target=main).start() #for increasing stack size for recurrsion


# *********************************************************** Q21

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
#     a = ['Messi', 'Cristiano', 'Pele', 'Maradona']
#     ans = sorted(a,key=len)
#     print(ans)
#     pass

# threading.Thread(target=main).start() #for increasing stack size for recurrsion



# *********************************************************** Q22


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
#     a = ['Kohli', 'Dhoni', 'Rohit', 'Kohli', 'Pant']
#     b=[]
#     ans=[]
#     for i in a:
#         if i not in b:
#             b.append(i)
#         elif i in b:
#             ans.append(i)
#     print(ans)
#     pass

# threading.Thread(target=main).start() #for increasing stack size for recurrsion



# *********************************************************** Q23



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
#     a="gravity is force and force is mass times acceleration"
#     dic = {}
#     b = a.split()
#     for i in b:
#         # if i !=' ':
#         if i not in dic:
#             dic[i]=1
#         else:
#             dic[i]+=1
#     print(dic)
#     pass

# threading.Thread(target=main).start() #for increasing stack size for recurrsion



# *********************************************************** Q24



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
#     patients = [25, 60, 45, 72, 15]
#     b=[]
#     for i in patients:
#         if(i>=60):
#             b.append('High')
#         elif(i>=40 and i<=59):
#             b.append('Medium')
#         else:
#             b.append('Low')
#     print(b)
#     pass

# threading.Thread(target=main).start() #for increasing stack size for recurrsion




# *********************************************************** Q25


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
    matches = [
    {'day': 'Mon', 'goals': [1, 2]},
    {'day': 'Tue', 'goals': [0, 3]},
    {'day': 'Wed', 'goals': [2, 2]}
    ]
    b={}
    for i in matches:
        b[i['day']]=sum(i['goals'])
    print(b)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion