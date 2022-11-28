n = list(input().split('-'))
starr = []
for i in range(len(n)):
    starr.append(n[i][0])
result = ''.join(s for s in starr)
print(result)
