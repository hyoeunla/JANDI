# 더하기 사이클

a = b = int(input())
count = 0
while True:
    ten = a // 10
    one = a % 10
    total = ten + one
    count = count + 1
    a = int(str(a % 10) + str(total % 10))
    if(b == a):
        break
print(count)
