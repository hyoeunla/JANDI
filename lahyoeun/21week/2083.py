while True:
    s = list(input().split())
    if int(s[1]) > 17 and int(s[2]) >= 80:
        print(s[0], "Senior")
    elif s[0] == "#" and s[1] == '0' and s[2] == '0':
        break
    else:
        print(s[0], "Junior")
