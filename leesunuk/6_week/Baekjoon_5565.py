# 영수증
hap = int(input())
book_moeny = []
for i in range(9):
    money = int(input())
    book_moeny.append(money)
for j in book_moeny:
    hap -= j
print(hap)
