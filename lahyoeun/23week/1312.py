a, b, n = map(int, input().split())
num = str(a / b)
c, count = num.split(".")
count = list(count)
if len(count) < n:
    print(0)
else:
    print(count[n-1])
'''
내 풀이 1 : 런타임에러 / 틀렸습니다
'''
a, b, n = map(int, input().split())
result = 0
for i in range(n):
    a = (a % b)*10
    result = a//b
print(result)
'''
내 풀이 2 : 파이썬 나누기는 소숫점이 1000자 이상 지원되지 않아서 생긴 문제 같음
따라서 직접 나눗셈을 구현해서 품 
'''
