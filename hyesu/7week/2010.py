# 플러그

import sys
input = sys.stdin.readline
n = int(input())
p = 1
for i in range(n):
    p += int(input())
print(p-n)
