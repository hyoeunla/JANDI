# 051 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요.(순위 정보는 저장하지 않습니다
moive_rank = ["닥터 스트레인지", "스플릿", "럭키"]

# 영화 제목은 문자열로 표현 가능, 
# 여러 개의 값을 저장하기 위해 리스트 자료형 사용

# 052 051의 movie_rank 리스트에 "배트맨"을 추가하라.
moive_rank = ["닥터 스트레인지", "스플릿", "럭키"]
moive_rank.append("배트맨")
print(moive_rank)
# append() : 리스트에 값 추가

# 053 moive_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
moive_rank = ["닥터 스트레인지", "스플릿","럭키", "배트맨"]
moive_rank.insert(1, "슈퍼맨")
print(moive_rank)
# insert(인덱스, 원소) : 특정 위치에 값을 끼어넣기 할 수 있다

# 054 moive_rank 리스트에서 '럭키'를 삭제하라.
moive_rank = ["닥터 스트레인지", "슈퍼맨", "스플릿", "럭키", "배트맨"]
del moive_rank[3] 
# del : 리스트에서 원소 삭제

# 055 moive_rank 리스트에서 '스플릿'과 '배트맨'을 삭제하라.
moive_rank = ["닥터 스트레인지", "슈퍼맨", "스플릿", "배트맨"]
del moive_rank[2] # 스플릿
del moive_rank[2] # 배트맨
# 여러 값을 삭제할 때 삭제된 후 남은 원소들에 대해서 순서를 새로 고려한 후 삭제해야 함

# 056 lang1과 lang2 리스트가 있을 대 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1+lang2
print(langs)

# 057 다음 리스트에서 최댓값과 최솟값을 출력하라.(힌트: min(), max() 함수 사용)
nums= [1,2,3,4,5,6,7]
print("max:",nums.max())
print("min:",nums.min())

# 058 다음 리스트의 합을 출력하라.
nums = [1,2,3,4,5]
print(sum(nums))

# 059 다음 리스트에 저장된 데이터의 개수를 화면에 구하라.
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))
# 060 다음 리스트의 평균을 출력하라.
nums = [1,2,3,4,5]
print(sum(nums)/len(nums))
avg = sum(nums) / len(nums)
print(avg)