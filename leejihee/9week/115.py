# 2. 왕실의 나이트
n = input()
col = int(ord(n[0])) - 96
row = int(n[1])
result = 0
step = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
# 이동할 수 있는 가지 수를 저장함

for i in step:
    n_col = col+i[0]  # i의 슬라이스는 x,y, step의 슬라이스는 좌표들
    n_row = row+i[1]
    if n_col >= 1 and n_col <= 8 and n_row >= 1 and n_row <= 8:
        result += 1
print(result)
