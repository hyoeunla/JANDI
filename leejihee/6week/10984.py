# 10984. 내 학점을 구해줘
semester = int(input())

for _ in range(semester):
    n = int(input())
    sum_c = 0
    sum_g = 0

    for _ in range(n):
        c, g = input().split()
        c = int(c)
        g = float(g)
        sum_c += c
        sum_g += g*c  # 학점평균 구하는 법 => (학점*점수의 합 / 총합점)
    print(sum_c, round(sum_g/sum_c, 1))
