# 2775 부녀회장이 될테야
testCase = int(input())

for i in range(testCase):
    k = int(input())
    n = int(input())
    
    arr = list(range(1,15))
    for _ in range(k):
        sum = 0
        for j in range(14):
            sum += arr[j]
            arr[j] = sum
    print(arr[n-1])


    # list
    # 1, 1+2, 1+2+3
    # 1, 1+3, 1+3+6

# 0층 1호 1명
#     2호 2명
#     3호 3명
# 1층 1호 1명
#     2호 3명
#     3호 6명
# 2층 1호 1명
#     2호 4명
#     3호 10명