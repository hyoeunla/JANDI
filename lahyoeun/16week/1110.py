n = int(input())
num = n
count = 0
while True:
    i = n % 10 + n//10
    n = (n % 10)*10 + i % 10
    count += 1
    if(n == num):
        break
print(count)
