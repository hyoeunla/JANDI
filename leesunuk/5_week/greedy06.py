# 6. 곱하기 혹은 더하기

n = list(map(int, input("숫자들을 입력해주세요: ")))
h = 0
for i in n:
    if i == 0 or i*h < i+h:
        h += i
    else:
        h *= i

print(h)
