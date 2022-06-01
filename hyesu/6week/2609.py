# 최대공약수와 최소공배수
import math

a, b = map(int, input().split())

print(math.gcd(a, b))  # Greatest Common Divisor(GCD)최대공약수
print(math.lcm(a, b))  # Least Common Multiple(LCM) 최소공배수
