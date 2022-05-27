n = int(input())
j = list(map(int, input().split()))

j.sort()  # j의 값들을 정렬해줌

hap = 0  # 총 그룹의 합
count = 0  # 그룹에 포함된 모험가 수

for i in j:
    count = count + 1
    if count >= i:
        hap = hap + 1
        count = 0

print(hap)
