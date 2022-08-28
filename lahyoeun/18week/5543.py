a = int(input())
b = int(input())
c = int(input())
coke = int(input())
soda = int(input())
s = []
s.append(a)
s.append(b)
s.append(c)
m = min(s)
if m + coke >= m+soda:
    print(m+soda-50)
else:
    print(m+coke-50)
