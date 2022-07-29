# 덱

import sys

n=int(sys.stdin.readline())
Deque=[]
for i in range(n):
    order=sys.stdin.readline().split()
    if order[0]=="push_front":
        Deque.insert(0, order[1])
    elif order[0]=="push_back":
        Deque.append(order[1])
    elif order[0]=="pop_front":
        if len(Deque) != 0:
            print(Deque[0])
            del(Deque[0])
        else:
            print(-1)
    elif order[0]=="pop_back":
        if len(Deque) != 0:
            print(Deque[-1])
            del(Deque[-1])
        else:
            print(-1)

    elif order[0]=="size":
        print(len(Deque))
    elif order[0]=="empty":
        if len(Deque)==0:
            print(1)
        else:
            print(0)
    elif order[0]=="front":
        if len(Deque) != 0:
            print(Deque[0])
        else:
            print(-1)
    elif order[0]=="back":
        if len(Deque) != 0:
            print(Deque[-1])
        else:
            print(-1)
    order=[]