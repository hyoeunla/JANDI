# 미래 도시

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 2차원 리스트를 만들고, 모든 값을 무한으로 초기화

for a in range(1, n + 1):   # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):     # 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
    a, b = map(int, input().split())  # a, b가 서로에게 가는 비용은 1이라고 설정
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())  # 거쳐 갈 노드 x와 최종 목적지 노드 k를 입력받기

for k in range(1, n + 1):      # 점화식에 따라 플로어드 워셜 알고리즘 수행
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]     # 수행된 결과를 출력

if distance >= INF:     # 도달할 수 없는 경우, -1을 출력
    print("-1")
else:                   # 도달할 수 있다면, 최단 거리를 출력
    print(distance)
