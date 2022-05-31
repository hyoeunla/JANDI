n = int(input(""))
at_book = [[]for _ in range(n)]

for i in range(n):
    human = list(map(str, input("").split()))
    at_book[i] = human

at_book.sort(key=lambda x: (x[3], x[2], x[1]))
print(at_book)
print(at_book[-1])
print(at_book[0])
