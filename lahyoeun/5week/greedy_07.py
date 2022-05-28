S = input()
change0 = 0  # 0으로 변하는 횟수
change1 = 0  # 1로 변하는 횟수

# case 1 문자열 S의 시작이 0이나 1인경우
if S[0] == 1:
    change0 += 1  # 만약 문자열 S의 처음이 1일 때 0으로 변하는 횟수 1 더해줌
else:
    change1 += 1  # 아니라면 1로 변하는 횟수 1 더해줌

for i in range(len[S]-1):  # 두번째 원소부터 확인
    if S[i] != S[i+1]:  # 현재 원소와 다음 원소가 다르다면
        if S[i+1] == 1:  # 다음 원소가 1이라면
            change0 += 1  # 0으로 바꾸는 횟수 1 증가
        else:
            change1 += 1  # 아니라면 1로 바꾸는 횟수 1 증가

print(min(change0, change1))  # 이들의 최솟값 출력
