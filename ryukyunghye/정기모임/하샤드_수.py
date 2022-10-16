# 프로그래머스 [12947] 하샤드 수
def solution(x):
    numberDigit = 0
    for i in str(x):
        numberDigit += int(i)
    return x % numberDigit == 0


def solution(x):
    numberList = list(str(x))
    numberDigit = 0
    for i in range(len(numberList)):
        numberDigit += int(numberList[i])
    return x % numberDigit == 0