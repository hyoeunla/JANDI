# 문제7. 문자열 뒤집기

s = input()
count0 = 0
count1 = 0

# 0으로 시작할 때, 1로 시작할 때 두가지 경우를 생각
if s[0] == '0':
    count0 += 1
elif s[0] == '1':
    count1 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:  # s[0] s[1]이 다르면 아래의 조건문을 실행
        if s[i+1] == '1':
            count1 += 1
        elif s[i+1] == '0':
            count0 += 1

print(min(count0, count1))  # 두 합 중 최솟값을 출력
