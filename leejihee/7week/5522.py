# 5522. 카드게임
sum = 0
for i in range(5):
    score = int(input())
    if score <= 100:  # 조건: 입력받은 점수가 0<A<100이어야 함
        sum += score
print(sum)
