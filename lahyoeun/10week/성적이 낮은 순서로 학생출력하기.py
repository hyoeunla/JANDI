N = int(input())
score = []
for i in range(N):
    input_score = input().split()
    # score에 입력받은 input_score을 나누어 하나는 문자형, 하나는 정수형으로 변환
    score.append((input_score[0], int(input_score[1])))

score = sorted(score, key=lambda student: student[1])
for student in score:
    print(student[0], end=' ')
