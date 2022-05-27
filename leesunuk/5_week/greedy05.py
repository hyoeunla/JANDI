# 5.모험가 길드

n = int(input("모험가가 몇명인지 입력해주세요: "))
x = list(map(int, input("각 모험가의 공포도를 입력해주세요: ").split()))

x.sort()
group = 0
count = 0

for i in x:
    count += 1
    if count >= i:
        group += 1
        count = 0
print(group)
