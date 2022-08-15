array = []
s = 0
n = 0
for i in range(9):
    array.append(int(input()))
    if s < array[i]:
        s = array[i]
        n = i+1
print(s)
print(n)
