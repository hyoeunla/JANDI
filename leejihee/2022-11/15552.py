# 15552 빠른 A+B
import sys

testCase = int(input())
for i in range(testCase):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)