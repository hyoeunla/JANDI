while True:
    n = input()
    count = 0
    if n == '#':
        break
    for i in n:
        if i in 'aeiouAEIOU':
            count += 1
    print(count)
