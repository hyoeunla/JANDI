array = [0, 1]
n = int(input())
for i in range(n-1):
    hap = array[i] + array[i+1]
    array.append(hap)
print(array[n])
