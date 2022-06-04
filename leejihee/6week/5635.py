# 5635. 생일

n = int(input())
studentList = []

for _ in range(n):
    student = input().split()  # 입력을 리스트로 받음
    student[1:] = list(map(int, student[1:]))
    studentList.append(student)  # 미리 정의한 리스트에 리스트를 넣으면 이중 리스트가 됨
studentList.sort(key=lambda student: (student[3], student[2], student[1]))
# 내림차순 다중 조건으로 정리하는 함수
# 일,월,년 순서이므로 기준을 뒤에서부터 정함

print(studentList[-1][0])  # 제일 어린 사람
print(studentList[0][0])  # 제일 나이 든 사람
