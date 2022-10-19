# 내 풀이 오류
n = int(input())
count = 0
etc = n % 5
if n % 5 == 0:
    count = n // 5
    print(count)
elif etc % 3 == 0:
    count = n // 5
    count += (etc // 3)
    print(count)
elif n % 3 == 0:
    count = n // 3
    print(count)
else:
    print("!")

# 다른 사람의 풀이
num = int(input())
count = 0

while num >= 0:
    if num % 5 == 0:
        count += int(num // 5)
        print(count)
        break

    num -= 3
    count += 1

else:
    print(-1)
