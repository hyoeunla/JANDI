n = input()
r = int(n[1])
c = int(ord(n[0])) - 96

d = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

dap = 0
for direction in d:
    n_r = r + direction[0]
    n_c = c + direction[1]
    if n_r >= 1 and n_r <= 8 and n_c >= 1 and n_c <= 8:
        dap += 1
print(dap)
