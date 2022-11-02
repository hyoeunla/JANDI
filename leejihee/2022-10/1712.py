a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    n = a/(c-b) + 1 
    print(int(n))