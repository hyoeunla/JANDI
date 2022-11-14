
def solution(line):
    line = list(line)
    li = []
    for i in line:
        if i in li:
            li.append("*")
        else:
            li.append(i)
    print(li)
    answer = ""
    answer.append(li[0])
    for j in range(1, len(li)):
        if li[j-1] != li[j]:
            answer.append(li[j])
    answer = "".join(str(s) for s in answer)
    return answer


print(solution("aabbbc"))
