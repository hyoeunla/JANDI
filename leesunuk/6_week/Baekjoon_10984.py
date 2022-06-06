# 내 학점을 구해줘
all_n = int(input(""))

for i in range(all_n):
    n = int(input(""))
    all_C = 0
    jumsu = 0

    for j in range(n):

        C, G = input("").split()
        C, G = int(C), float(G)
        all_C += C
        jumsu += (C*G)
    jumsu /= all_C
    print(all_C, round(jumsu, 1))
