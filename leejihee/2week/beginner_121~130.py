'''
121
사용자로부터 문자 한 개를 입력 받고, 
소문자일 경우 대문자로, 대문자 일 경우 소문자로 변경해서 출력하라.

>> a
A

힌트1 : islower() 함수는 문자의 소문자 여부를 판별합니다. 만약 소문자일 경우 True, 대문자일 경우 False를 반환합니다. 
힌트2 : upper() 함수는 대문자로, lower() 함수는 소문자로 변경합니다.
'''
ch = input()
if(ch.islower() == True):
    print(ch.upper())
else:
    print(ch.lower())

'''
122
점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 
사용자로부터 score를 입력받아 학점을 출력하라.

점수	학점
81~100	A
61~80	B
41~60	C
21~40	D
0~20	E
>> score: 83
grade is A
'''
score = int(input("score: "))
if(score > 80 and score <= 100):
    print('grade is A')
elif(score > 60 and score <= 80):
    print('grade is B')
elif(score > 40 and score <= 60):
    print('grade is C')
elif(score > 20 and score <= 40):
    print('grade is D')
else:
    print('grade is E')

'''
123
사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라. 
각 통화별 환율은 다음과 같다. 
사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.

통화명	환율
달러	1167
엔	    1.096
유로	1268
위안	171
>> 입력: 100 달러
116700.00 원
'''
money = input("돈 입력:").split()
if(money[1] == "달러"):
    print(int(money[0])*1167 + '원')
elif(money[1] == "엔"):
    print(int(money[0])*1.096 + '원')
elif(money[1] == "유로"):
    print(int(money[0])*1268 + '원')
elif(money[1] == "위안"):
    print(int(money[0])*171 + '원')

'''
124
사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.

>> input number1: 10
>> input number2: 9
>> input number3: 20
20
'''
