n = int(input())
array = []
array.append(1)  # 첫째 항을 배열에 저장
array.append(3)  # 두번째 항을 배열에 저장
if n == 1:
    print(1 % 10007)  # 1일경우
elif n == 2:
    print(3 % 10007)  # 2일경우
else:
    for i in range(n-2):  # 3 이상일 경우
        array.append(2*array[i]+array[i+1])
    print(array[-1] % 10007)
