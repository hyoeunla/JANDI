# [1977] 완전제곱수
m = int(input())
n = int(input())
numberList = [] 
for i in range(m,n+1):
    temp = int(i**0.5)
    if i == temp**2:
        numberList.append(i)

if numberList == []:
    print(-1)
else:
    print(f'{sum(numberList)}')
    print(f'{min(numberList)}')