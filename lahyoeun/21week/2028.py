n = int(input())
for i in range(n):
    a = input()
    b = str(int(a)*int(a))
    c = list(a)
    c = len(c)
    if str(a) == str(b[-c:]):
        print("YES")
    else:
        print('NO')
