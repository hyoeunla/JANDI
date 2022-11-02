m=int(input())
n=int(input())
arr=[]

for i in range(m,n+1):
    for j in range(1,n+1):
        if j**2==i:
            arr.append(i)

if len(arr)==0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])