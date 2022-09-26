a, b, c = map(int, input().split())
if c > b:
    print(int(a/(c-b)+1))
else:
    print(-1)
