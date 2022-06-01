n = int(input())
birth_li = []

for i in range(n):
    inform = input().split()
    inform[1:] = list(map(int, inform[1:]))
    birth_li.append(inform)

birth_li.sort(key=lambda x: (x[3], x[2], x[1]))
print(birth_li[-1][0])
print(birth_li[0][0])
