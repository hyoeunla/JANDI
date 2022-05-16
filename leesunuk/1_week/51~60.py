'''51번: 2016년 11월 영화 예매 순위 기준 top3(닥터 스트레인지, 스플릿, 럭키)를 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.) '''
movie_rank=["닥터 스트레인지", "스플릿", "럭키"]; print(movie_rank)

'''52번: 051의 movie_rank 리스트에 "배트맨"을 추가하세요.

내답: movie_rank=["닥터 스트레인지", "스플릿", "럭키", "배트맨"];print(movie_rank)

다른 방법: movie_rank=["닥터 스트레인지", "스플릿", "럭키"];movie_rank.append("배트맨"); print(movie_rank)

차이점: 내가 한 방법은 처음 변수를 선언할떄부터 배트맨을 추가해서 선언하는 방법이고, 다른 방법 같은경우엔 이미 변수를 지정한 뒤 나중에 추가하는 방식이다. '''

'''53번: movie_rank 리스트에는 movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']; movie_rank.insert(1, "슈퍼맨"); print(movie_rank) '''

'''54번: movie_rank 리스트에서 '럭키'를 삭제하라.

내답: movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']; movie_rank.delete("럭키"); print(movie_rank)

해답: movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']; del movie_rank[2]; print(movie_rank) '''

'''55번: movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라. (movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨'])'''

movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']; del movie_rank[2:]; print(movie_rank)

'''56번: lang1 = ["C", "C++", "JAVA"] 와 lang2 = ["Python", "Go", "C#"] 원소를 모두 가지고 있는  langs 리스트를 만들어라.

내답: lang1 = ["C", "C++", "JAVA"]; lang2 = ["Python", "Go", "C#"]; langs[lang1, lang2]; print(langs)

해답: lang1 = ["C", "C++", "JAVA"]; lang2 = ["Python", "Go", "C#"]; langs=lang1+lang2; print(langs) '''

'''57번: nums = [1, 2, 3, 4, 5, 6, 7] 에서 최솟값과 최댓값을 출력하라.

내답: 
nums = [1, 2, 3, 4, 5, 6, 7]
nm=min (nums)
nx=max (nums)
print("MAX:",nx) ; print("MIN:",nm)

다른방법:
nums = [1, 2, 3, 4, 5, 6, 7]
print("max: ", max(nums))
print("min: ", min(nums))
'''

'''58번: nums = [1, 2, 3, 4, 5] 리스트의 합을 출력하라'''
nums= [1, 2, 3, 4, 5]; s=sum(nums); print(s)

'''59번: cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]  데이터의 개수를 화면에 구하하라.

내답:
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
c= len(cook)
print(c)

다른방법:
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))
'''

'''60번: nums = [1, 2, 3, 4, 5]; 다음 리스트의 평균을 출력하라.
내답:
nums = [1, 2, 3, 4, 5]
s=sum(nums)
a=s/5
print(a)

다른 방법:
nums = [1, 2, 3, 4, 5]
average = sum(nums) / len(nums)
print(average)

차이점: 나눠줄때 len()메서드를 사용하지 않고 직접 리스트의 개수를 셌다.'''