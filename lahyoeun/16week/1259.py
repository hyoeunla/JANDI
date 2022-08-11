# 1번 방법
n = list(input())
while n != ['0']:
    if n == n[::-1]:
        print("yes")
    else:
        print("no")
    n = list(input())

# 2번 방법
n = int(input())
n1 = n
n_list = list(map(int, str(n)))
array = []
while n != 0:
    i = n1 % 10
    n1 = n1//10
    array.append(i)
    if n1 == 0 and n_list == array:
        print('yes')
        n = int(input())
        n1 = n
        array = []
        n_list = list(map(int, str(n)))
    elif n1 == 0 and n_list != array:
        print('no')
        n = int(input())
        n1 = n
        array = []
        n_list = list(map(int, str(n)))
