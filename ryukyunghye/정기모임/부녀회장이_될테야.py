# [2775] 부녀회장이 될테야
testCase = int(input())
for _ in range(testCase):
    floor = int(input())
    room = int(input())
    result = [i for i in range(1, room+1)]
    for i in range(floor):
        for j in range(1, room):
            result[j] += result[j-1]
    print(result[-1])