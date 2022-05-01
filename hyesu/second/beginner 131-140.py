'''
131
for문의 실행결과를 예측하라.

과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)
'''
# 리스트에 들어있는 문자열이 한 라인에 하나씩 출력됩니다.
#사과, 귤, 수박

'''
132
for문의 실행결과를 예측하라.

과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
  print("#####")
'''
# 저장된 데이터 개수만큼 반복된다
#####
#####
#####

'''
133
다음 for 문과 동일한 기능을 수행하는 코드를 작성하세요.

for 변수 in ["A", "B", "C"]:
  print(변수)
'''
var = "A"
print(var)
var = "B"
print(var)
var = "C"
print(var)

'''
134
for문을 풀어서 동일한 동작을하는 코드를 작성하라.

for 변수 in ["A", "B", "C"]:
  print("출력:", 변수)
'''
var = "A"
print("출력:", var)
var = "B"
print("출력:", var)
var = "C"
print("출력:", var)

'''
135
for문을 풀어서 동일한 동작을 하는 코드를 작성하라.

for 변수 in ["A", "B", "C"]:
  b = 변수.lower()
  print("변환:", b)
'''
var = "A"
b = var.lower()
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
for var in [10, 20, 30]:
    print(var)

'''
137
다음 코드를 for문으로 작성하라.

print(10)
print(20)
print(30)
'''
for 변수 in [10, 20, 30]:
    print(변수)

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
for var in [10, 20, 30]:
    print(var)
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
for var in [10, 20, 30]:
    print(var)

'''
140
다음 코드를 for문으로 작성하라.

print("-------")
print("-------")
print("-------")
print("-------")
'''
for var in [1, 2, 3, 4]:
    print("-------")
