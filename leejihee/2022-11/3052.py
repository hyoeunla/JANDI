# 3052 나머지
arr = [int(input()) for i in range(10)]
rem = []
for i in arr:
    rem.append(i % 42)
print(len(set(rem)))