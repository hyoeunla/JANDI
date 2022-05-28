# 07. 문자열 뒤집기_백준 1439번

# 내 풀이 -> 0과 1을 구분해서 받음
s = input()
zero = 0
one = 0
if s[0] == '0':
    zero += 1
else:
    one += 1
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            zero += 1
        else:
            one += 1
print(min(zero, one))

# 다른 풀이 -> 0과 1 구분 없이 하나에 받음
s = input()
count = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count += 1
print((count + 1) // 2)

# 답안
data = input()
count0 = 0
count1 = 1
if data[0] == '1':
    count0 += 1
else:
    count1 += 1
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1
print(min(count0, count1))
