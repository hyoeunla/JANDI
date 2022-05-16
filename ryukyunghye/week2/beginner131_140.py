# 131. for문의 실행결과를 예측하라.
fruit = ["사과", "귤", "수박"]
for i in fruit:
    print(i)
# 사과 귤 수박 순으로 출력

# 132.  for문의 실행결과를 예측하라.
fruit = ["사과", "귤", "수박"]
for i in fruit:
    print("#####")
# #####가 3번 출력됨

# 133. 다음 for문과 동일한 기능을 수행하는 코드를 작성하세요.
for i in ["A", "B", "C"]:
    print(i)
# 방법1
print("A")
print("B")
print("C")
# 방법2
i = "A"
print(i)
i = "B"
print(i)
i = "C"
print(i)

# 134. for문을 풀어서 동일한 동작을 하는 코드를 작성하라.
for i in ["A", "B", "C"]:
    print("출력:", i)
# 방법1
print("출력:", "A")
print("출력:", "B")
print("출력:", "C")
# 방법2
i = "A"
print("출력:", i)
i = "B"
print("출력:", i)
i = "C"
print("출력:", i)

# 135. for문을 풀어서 동일한 동작을 하는 코드를 작성하라.
for i in ["A", "B", "C"]:
    b = i.lower()
    print("변환:", b)
# 방법1
print("변환:", "A".lower())
print("변환:", "B".lower())
print("변환:", "C".lower())
# 방법2
i = ("A").lower()
print("변환:", i)
i = ("B").lower()
print("변환:", i)
i = ("C").lower()
print("변환:", i)

# 136&137. 다음 코드를 for문으로 작성하라.
for i in [10, 20, 30]:
    print(i)

# 138. 다음 코드를 for문으로 작성하라.
for i in [10, 20, 30]:
    print(i)
    print("------")

# 139. 다음 코드를 for문으로 작성하라.
print("++++")
for i in [10, 20, 30]:
    print(i)

# 140. 다음 코드를 for문으로 작성하라.
for i in [1, 2, 3, 4]:
    print("------")
