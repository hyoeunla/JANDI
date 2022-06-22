# 시각
# 방법1
n = int(input())
count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1
print(count)

# 방법2
n = int(input())
h = 0
s = 0
m = 0
count = 0
for i in range((n+1)*3600):
    h = i // 3600
    m = (i % 3600) // 60
    s = i % 60
    if '3' in str(h)+str(m)+str(s):
        count += 1
print(count)
