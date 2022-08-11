n = list(input())
while n != ['0']:
    if n == n[::-1]:
        print("yes")
    else:
        print("no")
    n = list(input())
