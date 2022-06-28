# 성적이 낮은 순서로 학생 출력하기
n = int(input())
result = []
for i in range(n):
    result.append(input().split())
result.sort(key=lambda score: score[1])
for i in range(n):
    print(result[i][0], end=" ")
