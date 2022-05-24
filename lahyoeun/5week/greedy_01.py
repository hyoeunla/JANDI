charge = 1260
n = 0
n = charge // 500
s = ((charge)-500*n) // 100
k = (((charge)-500*n) - 100*s) // 50
l = ((((charge)-500*n) - 100*s) - 50*k) // 10
print(n+s+k+l)
