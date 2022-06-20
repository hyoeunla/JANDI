# 7. 럭키 스트레이트
n = input()
result1 = 0
result2 = 0

for i in range(len(n)//2):
    result1 += int(n[i])
for i in range(1, (len(n)//2)+1):
    result2 += int(n[len(n)-i])

if result1 == result2:
    print("LUCKY")
else:
    print("READY")
