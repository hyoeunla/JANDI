'''
131번: for문의 실행결과를 예측하라.
'''

과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)

'''
내답:
사과
귤
수박
'''

'''
132번: for문의 실행결과를 예측하라.
'''
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print("#####")

'''
#####
#####
#####
'''

'''
133번: 다음 for 문과 동일한 기능을 수행하는 코드를 작성하세요.
'''
for 변수 in ["A", "B", "C"]:
    print(변수)


변수 = "A"
print(변수)
변수 = "B"
print(변수)
변수 = "C"
print(변수)

'''
134번: for문을 풀어서 동일한 동작을하는 코드를 작성하라.
'''
for 변수 in ["A", "B", "C"]:
    print("출력:", 변수)

변수 = 'A'
print("출력: ", 변수)
변수 = 'B'
print("출력: ", 변수)
변수 = 'C'
print("출력: ", 변수)

'''
135번: for문을 풀어서 동일한 동작을 하는 코드를 작성하라.
'''
for 변수 in ["A", "B", "C"]:
    b = 변수.lower()
    print("변환:", b)

변수 = 'A'
print("변환: ", 변수.lower())
변수 = 'B'
print("변환: ", 변수.lower())
변수 = 'C'
print("변환: ", 변수.lower())

'''
136번: 다음 코드를 for문으로 작성하라.
'''
변수 = 10
print(변수)
변수 = 20
print(변수)
변수 = 30
print(변수)


변수 = 0
for a in range(0, 3):
    변수 += 10
    print(변수)

'''
137번: 다음 코드를 for문으로 작성하라.
'''
print(10)
print(20)
print(30)

a = 0
for i in range(0, 3):
    a += 10
    print(a)

'''
138번: 다음 코드를 for문으로 작성하라.
'''
print(10)
print("-------")
print(20)
print("-------")
print(30)
print("-------")

for i in ["10", "20", "30"]:
    print(i)
    print("-------")

'''
139번: 다음 코드를 for문으로 작성하라.
'''
print("++++")
print(10)
print(20)
print(30)

a = 0
print("++++")
for i in range(0, 3):
    a += 10
    print(a)


'''
140번: 다음 코드를 for문으로 작성하라.
'''
print("-------")
print("-------")
print("-------")
print("-------")

for i in range(0, 4):
    print("-------")
