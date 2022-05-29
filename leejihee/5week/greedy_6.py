# 문제6. 곱하기 혹은 더하기

# 나의 풀이
s = input()
result = 1
for i in s:
    if int(i) <= 1:
        result += int(i)
    else:
        result *= int(i)
print(result)

# 해설
s = input()
result = int(s[0])  # 첫번째 숫자를 우선 대입
for i in range(1, len(s)):  # 남은 데이터만큼 계산
    num = int(s[i])
    if num <= 1 or result <= 1:  # 다음 수가 0,1인 경우는 더하기로하는게 더 큼
        result += num
    else:
        result *= num
print(result)
