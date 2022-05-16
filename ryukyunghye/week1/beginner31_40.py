# 031 문자열 합치기
a = "3"
b = "4"
print(a+b)  # 34
# -> "34"라는 새로운 문자열이 생기고 그 값이 print함수에 의해 출력됨

# 032 문자열 곱하기
print("Hi"*3)  # HiHiHi
# -> 문자열에 대한 곱셈은 문자열의 반복을 의미한다

# 033 문자열 곱하기
print('-' * 80)

# 034 문자열 곱하기
t1 = 'python'
t2 = 'java'
t = t1+' '+t2+' '
print(t * 4)

# 035 문자열 출력
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))
# C style처럼 사용 가능

# 036 문자열 출력
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".foramt(name2, age2))
# {}에 대응하는 것을 format()의 인자로 전달할 수 있다

# 037 문자열 출력
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: {name1} 나이: {age1}")
print("이름: {name1} 나이: {age2}")
# formatting 스타일과 유사, {}에 변수를 직접 입력

# 038 컴마 제거하기
number = "5,969,782,550"
comma = number.replace(",", "")
print(int(comma), type(int(comma)))
# replace(old, new, [count]) : 문자열 안의 특정 문자를 새로운 문자로 변경하는 기능을 가짐
# old : 변경하고 싶은 문자
# new : 새로 바꿀 문자
# count : 변경할 횟수

# 039 문자열 슬라이싱
part = "2020/03(E) (IFRS 연결)"
print(part[7:])

# 040 strip 메서드
data = "  삼성전자  "
print(data.strip())
space = data.strip()
print(space)
# strip([chars]) : 인자로 전달된 문자를 string의 왼쪽과 오른쪽에서 제거한다