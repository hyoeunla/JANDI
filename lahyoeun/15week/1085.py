x, y, w, h = map(int, input().split())
min_l = []
if x < + (w-x):
    min_l.append(x)
else:
    min_l.append(w-x)
if y <= (h-y):
    min_l.append(y)
else:
    min_l.append(h-y)
print(min(min_l))
