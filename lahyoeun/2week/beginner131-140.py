'''
131
for문의 실행결과를 예측하라.

과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)
'''
# 사과
# 귤
# 수박

'''
132
for문의 실행결과를 예측하라.

과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
  print("#####")
'''
'''
정답
#####
#####
#####
'''

'''
133
다음 for 문과 동일한 기능을 수행하는 코드를 작성하세요.

for 변수 in ["A", "B", "C"]:
  print(변수)
'''
변수 = "A"
print(변수)
변수 = "B"
print(변수)
변수 = "C"
print(변수)


'''
134
for문을 풀어서 동일한 동작을하는 코드를 작성하라.

for 변수 in ["A", "B", "C"]:
  print("출력:", 변수)
'''
변수 = "A"
print("출력:", 변수)
변수 = "B"
print("출력:", 변수)
변수 = "C"
print("출력:", 변수)


'''
135
for문을 풀어서 동일한 동작을 하는 코드를 작성하라.

for 변수 in ["A", "B", "C"]:
  b = 변수.lower()
  print("변환:", b)
'''
변수 = "A"
b = 변수.lower()
print("변환:", b)
변수 = "B"
b = 변수.lower()
print("변환:", b)
변수 = "C"
b = 변수.lower()
print("변환:", b)


'''
136
다음 코드를 for문으로 작성하라.

변수 = 10
print(변수)
변수 = 20
print(변수)
변수 = 30
print(변수)
'''
for 변수 in ["10", "20", "30"]:
    print(변수)


'''
137
다음 코드를 for문으로 작성하라.

print(10)
print(20)
print(30)
'''
for i in [10, 20, 30]:
    print(i)


'''
138
다음 코드를 for문으로 작성하라.

print(10)
print("-------")
print(20)
print("-------")
print(30)
print("-------")
'''
for i in [10, 20, 30]:
    print(i)
    print("-------")


'''
139
다음 코드를 for문으로 작성하라.

print("++++")
print(10)
print(20)
print(30)
'''
print("++++")
for i in [10, 20, 30]:
    print(i)


'''
140
다음 코드를 for문으로 작성하라.

print("-------")
print("-------")
print("-------")
print("-------")
'''
for i in [10, 20, 30, 40]:
    print("-------")
