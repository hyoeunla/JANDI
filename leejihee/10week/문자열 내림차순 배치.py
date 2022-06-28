# 문자열 내림차순으로 배치하기
# 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
# s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

# 나의 풀이
def solution(s):
    list = []
    for i in s:
        list.append(i)
    list.sort(reverse=True)
    result = ''.join(list)
    return result


# 다른 풀이(1)
def solution1(s):
    list = list(s)  # 문자열을 list함수로 묶으면 문자 하나하나 리스트에 저장됨
    list.sort(reverse=True)
    result = ''.join(list)
    return result


# 다른 풀이 (2)
def solution2(s):
    list = list(s)
    result = ''.join(sorted(list, reverse=True))  # sorted 함수로 내림차순 정리를 할 수 있음
    return result
