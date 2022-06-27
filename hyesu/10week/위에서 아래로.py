# 위에서 아래로

n = int(input())  # n을 입력받기

array = []       # n개의 정수를 입력받아 리스트에 저장
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)  # 파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행

for i in array:  # 정렬이 수행된 결과를 출력
    print(i, end=' ')
