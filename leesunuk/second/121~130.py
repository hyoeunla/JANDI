'''
121:번: 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.
'''
a = input("문자 한개를 입력해주세요: ")
b = a.islower()
if b == True:
    print(a.upper())
else:
    print(a.lower())

'''
또 다른 방법
'''
a = input("")
if a.islower():
    print(a.upper())
else:
    print(a.lower())

'''
122번: 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.
(A(81~100), B(61~80), C(41~60), D(21~40), E(0~20))
'''
score = input("점수를 입력해주세요: ")
iscore = int(score)
if iscore > 80:
    print("grade is A")
elif 81 > iscore > 60:
    print("grad is B")
elif 61 > iscore > 40:
    print("grad is C")
elif 41 > iscore > 20:
    print("grad is D")
else:
    print("grad is E")

'''
123번: 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라. 각 통화별 환율은 다음과 같다. 
 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.
달러    1167
엔     1.096
유로    1268
위안	171
'''
HW = {"달러": 1167, "엔": 1.086, "유로": 1268, "위안": 171}
a = input("입력: ")
b, c = a.split()
print(float(b) * HW[c], "원")
