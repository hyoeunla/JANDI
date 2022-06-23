hour = int(input())
count = 0  # count해주는 변수 설정
for i in range(hour+1):  # 시
    for j in range(60):  # 분
        for k in range(60):  # 초
            if '3' in str(i)+str(j)+str(k):  # 전체 시 분 초에 3 세기
                count += 1
print(count)
