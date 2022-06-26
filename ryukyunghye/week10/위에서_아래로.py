# 위에서 아래로
n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
array.sort(reverse=True)
# array= sorted(array, reverse = True)
print(*array)
