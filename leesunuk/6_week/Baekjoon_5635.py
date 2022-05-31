n = int(input(""))
at_book = []

for i in range(n):
    human = input().split()
    human[1:] = (list(map(int, human[1:])))
    at_book.append(human)

at_book.sort(key=lambda x: (x[3], x[2], x[1]))
print(at_book[-1][0])
print(at_book[0][0])
