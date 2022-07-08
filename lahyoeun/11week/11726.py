n = int(input())
array = []
array.append(1)  # 첫째 항을 배열에 저장
array.append(2)  # 두번째 항을 배열에 저장
if n == 1:
    print(1 % 10007)  # 1일경우
elif n == 2:
    print(2 % 10007)  # 2일경우
else:
    for i in range(n-2):  # 3 이상일 경우
        array.append(array[i]+array[i+1])  # (n-1)+(n-2)의 값을 배열에 저장해줌
    print(array[-1] % 10007)  # 마지막 배열의 값을 가져오고 나머지 연산 실행, 출력
