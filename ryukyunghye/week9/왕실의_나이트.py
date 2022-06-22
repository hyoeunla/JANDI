# 왕실의 나이트
now_position = list(input())
now_x = ord(now_position[0])
now_y = int(now_position[1])
result = 0
positions = [(-2, -1), (-1, -2), (1, -2), (2, -1),
             (2, 1), (1, 2), (-1, 2), (-2, 1)]
for position in positions:
    move_x = now_x + position[0]
    move_y = now_y + position[1]
    if ord('a') <= move_x <= ord('h') and 1 <= move_y <= 8:
        result += 1
print(result)
