n = []
for i in range(10):
    s = (int(input()) % 42)
    if s not in n:
        n.append(s)
print(len(n))
