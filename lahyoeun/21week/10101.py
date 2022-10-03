a = int(input())
b = int(input())
c = int(input())
d = a+b+c
if a == 60 and b == 60 and c == 60:
    print("Equilateral")
elif (d == 180) and ((a == b) or (b == c) or (a == c)):
    print("Isosceles")
elif d == 180 and (a != b != c):
    print("Scalene")
elif d != 180:
    print("Error")
