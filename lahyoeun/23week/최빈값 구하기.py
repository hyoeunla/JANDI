array = map(int, input().split())
a = max(array)
count = [0]*a
for i in array:
    count[i-1] += 1
