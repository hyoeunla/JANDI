# 141. 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 for 문을 사용해서 화면에 출력하라. 단 부가세는 10원으로 가정한다.
aList = [100, 200, 300]
for i in aList:
    print(i+10)

# 142. for 문을 사용해서 리스트에 저장된 값을 다음과 같이 출력하라.
aList = ["김밥", "라면", "튀김"]
for i in aList:
    print("오늘의 메뉴:", i)

for i in aList:
    print("오늘의 메뉴: "+i)

# 143. 리스트에 주식 종목이름이 저장돼 있다. 저장된 문자열의 길이를 다음과 같이 출력하라.
aList = ["SK하이닉스", "삼성전자", "LG전자"]
for i in aList:
    print(len(i))

# 144. 리스트에는 동물 이름이 문자열로 저장돼 있다. 동물 이름과 글자수를 다음과 같이 출력하라.
aList = ['dog', 'cat', 'parrot']
for i in aList:
    print(i, len(i))


# 145. 리스트에는 동물 이름이 문자열로 저장돼 있다. for문을 사용해서 동물 이름의 첫 글자만 출력하라.
aList = ['dog', 'cat', 'parrot']
for i in aList:
    print(i[0])

# 146.  리스트에 세 개의 숫자가 바인딩돼 있다. for문을 사용해서 다음과 같이 출력하라.
aList = [1, 2, 3]
for i in aList:
    print("3 x", i)

for i in aList:
    print("3 x"+str(i))

# 147. 리스트에는 세 개의 숫자가 바인딩돼 있다. for문을 사용해서 다음과 같이 출력하라.
aList = [1, 2, 3]
for i in aList:
    print("3 x", i, "=", 3*i)

for i in aList:
    print("3 x {} = {}".format(i, 3*i))

# 148. 리스트에는 네 개의 문자열이 바인딩돼 있다. for문을 사용해서 다음과 같이 출력하라.
aList = ["가", "나", "다", "라"]
# 방법1
for i in aList[1:]:
    print(i)

bList = aList[1:]
for i in bList:
    print(i)

# 149. 리스트에는 네 개의 문자열이 바인딩돼 있다. for문을 사용해서 다음과 같이 출력하라.
aList = ["가", "나", "다", "라"]
for i in aList[::2]:
    print(i)

# 150. 리스트에는 네 개의 문자열이 바인딩돼 있다. for문을 사용해서 다음과 같이 출력하라.
aList = ["가", "나", "다", "라"]
for i in aList[::-1]:
    print(i)
