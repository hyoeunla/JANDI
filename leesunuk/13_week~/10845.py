# 큐

import sys

queue=[]
n=int(sys.stdin.readline())

for i in range(n):
    order= sys.stdin.readline().split()
    
    if order[0]=="push":
        queue.append(order[1])
    elif order[0]=="pop":
        if len(queue) !=0:
            print(queue[0])
            del(queue[0])
        else:
            print(-1)
    elif order[0]=="size":
        print(len(queue))
    elif order[0]=="empty":
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif order[0]=="front":
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif order[0]=="back":
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)
    order=[]