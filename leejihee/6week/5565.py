# 5565. 영수증
value = int(input())  # 총 값이 주어짐 (9850)
for i in range(9):
    book = int(input())
    value -= book
print(value)
