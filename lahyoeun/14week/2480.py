n = list(map(int, input().split()))
if n[0] == n[1] == n[2]:
    print(10000+n[0]*1000)
elif n[0] == n[1] or n[0] == n[2]:
    print(1000+n[0]*100)
elif n[2] == n[1]:
    print(1000+n[1]*100)
else:
    print(max(n)*100)
