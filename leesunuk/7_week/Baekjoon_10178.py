# 할로윈의 사탕

n = int(input())

for i in range(n):
    hap, candy = map(int, input().split())
    print("You get", hap//candy, "piece(s) and your dad gets", hap %
          candy, "piece(s).")
