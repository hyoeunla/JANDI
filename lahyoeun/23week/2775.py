t = int(input())
for i in range(t):
    floor = int(input())
    n = int(input())
    people = [i for i in range(1, n+1)]
    for j in range(floor):
        for k in range(1, n):
            people[k] = people[k] + people[k-1]
    print(people[n-1])
