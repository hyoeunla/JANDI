# 핸드폰 번호 가리기

def solution(phone_number):
    pn_back = phone_number[-4:]
    phone_number = len(phone_number)-len(pn_back)
    answer = "*"*phone_number+pn_back
    return answer
