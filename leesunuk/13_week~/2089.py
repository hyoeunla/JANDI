# -2진수

n=int(input())
answer=''
if n==0:
    print(0)
    
while n!=0:
    if n%-2 == -1:
        n=n//-2+1
        answer='1'+answer
    else:
        n//=-2
        answer='0'+answer

print(answer)