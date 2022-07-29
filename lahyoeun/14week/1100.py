board = [0] * 9
count = 0
for i in range(8):
    board[i] = list(input())
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0 and board[i][j] == 'F':
            count += 1
        if i % 2 != 0 and j % 2 != 0 and board[i][j] == 'F':
            count += 1
print(count)
