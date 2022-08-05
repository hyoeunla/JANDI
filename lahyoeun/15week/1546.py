n = int(input())
m = 0
hap = 0
array = list(map(int, input().split()))
m = max(array)
for i in array:
    hap += i/m*100

print(hap/n)
