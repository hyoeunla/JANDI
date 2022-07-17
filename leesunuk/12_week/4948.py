# 베르트랑 공준

while 1:
    n = int(input())
    if (n != 0 and n > 1):
        result_sub = 0
        result = []
        for i in range(n+1, n*2+1):
            for j in range(2, n):
                if i % j == 0:
                    result_sub = 0
                    break
                else:
                    result_sub = i
            if result_sub != 0:
                result.append(result_sub)
        print(len(result))
    elif n == 1:
        print(n)
    else:
        break
# 시간 초과 문제로 다시 고민해보는 중
