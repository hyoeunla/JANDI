n, m, o = map(int, input().split())
while n != 0 and m != 0 and o != 0:
    if n*n == m*m + o*o or m*m == n*n + o*o or o*o == n*n+m*m:
        print("right")
        n, m, o = map(int, input().split())
    else:
        print("wrong")
        n, m, o = map(int, input().split())
