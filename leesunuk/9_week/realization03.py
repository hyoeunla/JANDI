# 왕실의 나이트
n = input()
x = ord(n[0])
y = int(n[1])
way = {(-2, -1), (-1, -2), (1, -2), (2, -1), (-1, 2), (-2, 1), (1, 2), (2, 1)}
result = 0

for i in way:
    wayX = x+i[0]
    wayY = y+i[1]
    if wayX >= 97 and wayX <= 104 and wayY >= 1 and wayY <= 8:
        result += 1

print(result)
