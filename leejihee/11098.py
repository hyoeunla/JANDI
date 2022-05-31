n = int(input())


for _ in range(n):
    p = int(input())
    clist = []
    namelist = []
    for _ in range(p):
        c, name = input().split()
        c = int(c)
        clist.append(c)
        namelist.append(name)

    # 각각 비용리스트, 선수리스트에 넣었고 높은 비용에 맞는 선수를 출력해야함
    # 한번에 출력하는 것이 아니라 p가 끝날 때마다 출력
    idx = clist.index(max(clist))  # index 함수 정리
    print(namelist[idx])
