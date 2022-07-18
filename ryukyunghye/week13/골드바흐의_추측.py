# [6588] 골드바흐의 추측
import sys
numberList = [True] * 1000001
for i in range(2, int((1000000)**0.5)+1):
    if numberList[i]:
        for j in range(i*2, 1000000, i):
            numberList[j] = False
while True:
    inputNumber = int(sys.stdin.readline())
    if inputNumber == 0:
        break
    count = 0
    for k in range(3, len(numberList)):
        if numberList[k] and numberList[inputNumber-k]:
            print(f'{inputNumber} = {k} + {inputNumber-k}')
            count = 1
            break
    if count == 0:
        print("Goldbach's conjecture is wrong.")
