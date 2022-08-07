count = 0
for i in range(3):
    array = list(input().split())
    for j in array:
        if j == "1":
            count += 1
    if count == 0:
        print("D")
    elif count == 1:
        print("C")
    elif count == 2:
        print("B")
    elif count == 3:
        print("A")
    else:
        print("E")
    count = 0
