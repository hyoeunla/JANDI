# 05. 모험가 길드

n = int(input())
x = list(map(int, input().split()))
x.sort()
group = 0
member = 0
for i in x:
    member += 1
    if member >= i:
        group += 1
        member = 0
print(group)


n = int(input())
x = list(map(int, input().split()))
x.sort() 	        # 오름차순 정리, 내림차순 불가능
group = 0	   	    # 나눌 그룹의 수
member = 0 			# 각 그룹의 사람 수
for i in x:
    member += 1  # 현재 그룹에 사람 추가
    if member >= i:  # 현재 그룹에 포함된 모험가 수가 현재 공포도보다 크거나 같으면
        group += 1  # 그룹 생성
        member = 0  # 이전 그룹은 마무리, 다음 그룹 생성을 위해 사람 수 초기화
print(group)
