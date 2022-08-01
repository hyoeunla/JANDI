'''a, b = input().split()
str_A = list(a)
str_B = list(b)
A = list(map(int, str_A))
B = list(map(int, str_B))
hap = 0
if len(A) > len(B):
    for i in A:
        for j in B:
            hap += i * j
else:
    for i in B:
        for j in A:
            hap += i * j
print(hap)'''

a, b = input().split()
str_A = list(a)
str_B = list(b)
A = list(map(int, str_A))
B = list(map(int, str_B))
a_hap = 0
b_hap = 0
for i in A:
    a_hap += i
for j in B:
    b_hap += j
print(a_hap*b_hap)
