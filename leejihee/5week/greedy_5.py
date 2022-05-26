# 문제5. 모험가 길드

# 해설의 도움을 받은 풀이
n = int(input())
x = sorted(map(int, input().split()))  # 1 2 2 2 3으로 정렬됨
count = 0  # 그룹의 수
p = 0  # 그룹 안의 모험가 수

for i in range(n):
    p += 1  # 모험가 한명씩 추가
    if p >= x[i]:  # 모험가가 공포도보다 많거나 같을 경우 그룹 결성
        count += 1
        p = 0
print(count)  # 1 / 2 2 / (보류 2 3) 두 팀으로 결성

# 해설
n = int(input())
x = sorted(map(int, input().split()))
count = 0
p = 0

for i in x:  # 리스트 x를 범위로 해서 i로 하나씩 호출
    p += 1
    if p >= i:
        count += 1
        p = 0
print(count)
