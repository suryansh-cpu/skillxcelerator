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
#     a ={'key1':'value1','value1':'key2','value3':'key1'}
#     ans = {}
#     for i in a:
#         # print(i)
#         # print(a[i])
#         if i not in ans:
#             ans[i] = {}
#         if 'key' not in ans[i]:
#             ans[i]['key'] = 0
#         if a[i] not in ans:
#             ans[a[i]] = {}
#         if 'value'not in ans[i]:
#             ans[a[i]]['value'] = 0
#         ans[i]['key'] += 1
#         ans[a[i]]['value']+=1
#         # if(i in ans):
#         #     ans[i]['key']+=1
#         # elif(a[i] in ans):
#         #     ans[a[i]]['value']+=1
#         # elif(not(i in ans)):
#         #     ans[i]['key']+=1
#         # elif(not(a[i] in ans)):
#         #     ans[a[i]]['value']+=1
#     print(ans)
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
    a ={'key1':'value1','value1':'key2','value3':'key1'}
    ans = {}
    for i in a:
        if(i not in ans):
            ans[i]={'key':1,'value':0}
        elif(i in ans):
            ans[i]['key']+=1
        if(a[i] not in ans):
            ans[a[i]]={'key':0,'value':1}
        else:
            ans[a[i]]['value']+=1
    print(ans)
    pass

threading.Thread(target=main).start() #for increasing stack size for recurrsion