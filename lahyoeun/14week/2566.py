n = 0
x = 0
y = 0
array = [0]*9
for i in range(9):
    array[i] = list(map(int, input().split()))
    for j in range(9):
        if array[i][j] > n:
            n = array[i][j]
            x = i
            y = j
print(n)
print(x+1, y+1)
