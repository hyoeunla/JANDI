# [이코테] 1로 만들기
number = int(input())
table = [0] * 30001
for i in range(2, number+1):
    table[i] = table[i-1] + 1
    if i % 5 == 0:
        table[i] = min(table[i], table[i//5]+1)
    if i % 3 == 0:
        table[i] = min(table[i], table[i//3]+1)
    if i % 2 == 0:
        table[i] = min(table[i], table[i//2]+1)
print(table[number])
