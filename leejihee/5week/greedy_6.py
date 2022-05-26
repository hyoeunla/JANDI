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

# 풀이 흔적들...
# for i in range(len(s)-1):
#     hap = int(s[i])+int(s[i+1])
#     gob = int(s[i])*int(s[i+1])
#     result = hap if hap > gob else gob
#     result +=s[i]
#     result *=s[i]

# for i in range(len(s)-1):
#     hap = int(s[i])+int(s[i-1])
#     gob = int(s[i])*int(s[i-1])
#     if hap > gob:
#         result += int(s[i-1])
#     else:
#         result *= int(s[i-1])
# print(result)

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
