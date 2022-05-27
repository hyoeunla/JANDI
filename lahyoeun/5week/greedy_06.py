S = input()
dap = int(S[0])

for i in range(1, len(S)):
    cal = int(S[i])
    if cal <= 1 or dap <= 1:
        dap += cal
    else:
        dap *= cal

print(dap)
