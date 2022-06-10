import sys
N = int(sys.stdin.readline())
hap = 0
for i in range(N):
    s = int(sys.stdin.readline())
    hap += s
    flug = hap - (N-1)
print(flug)
