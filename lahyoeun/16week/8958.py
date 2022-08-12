n = int(input())
hap = 0
k = 0
for i in range(n):
    dap = list(input())
    for j in dap:
        if j == "O":
            k += 1
            hap += k
        else:
            k = 0
    print(hap)
    hap = 0
    k = 0
