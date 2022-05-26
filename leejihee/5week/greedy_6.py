# 문제6. 곱하기 혹은 더하기

# 나의 풀이
s = input()
result = 1
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

for i in s:
    if int(i) <= 1:
        result += int(i)
    else:
        result *= int(i)
print(result)

# 해설