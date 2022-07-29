

def solution(seoul):
    # seoul = list(input().split())
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return (f"김서방은 {i}에 있다")


solution(["Jane", "Kim"])
