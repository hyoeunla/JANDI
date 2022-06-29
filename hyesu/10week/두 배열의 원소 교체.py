# 두 배열의 원소 교체

n, k = map(int, input().split())     # N과 K를 입력받기
a = list(map(int, input().split()))  # 배열 A의 모든 원소를 입력받기
b = list(map(int, input().split()))  # 배열 B는 모든 원소를 입력받기

a.sort()              # 배열 A는 오름차순 정렬 수행
b.sort(reberse=True)  # 배열 B는 내림차순 정렬 수행

for i in range(k):    # 첫 번쨰 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
    if a[i] < b[i]:   # A의 원소가 B의 원소보다 작은 경우

        a[i], n[i] = b[i], a[i]    # 두 원소를 교체
    else:         # A의 우너소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a))  # 배열 A의 모든 원소의 합을 출력
