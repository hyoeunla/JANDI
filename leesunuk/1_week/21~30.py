'''21번: letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요. (letters = 'python')
내답: letters='python';print(letters(1,3))
이렇게 생각한 이유: letters에 python 문자열이 저장되어 있는데 이 문자열에서 첫번째와 세번쨰 문자를 출력해야 된다는 것을
너무 단순하게 생각한 거 같다.

해답: letters='python';print(lang[0], lang[2])
'''

'''22번: 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요. (license_plate = "24가 2210")
내답: license_plate="24가 2210";print(license_plate[4],license_plate[5],license_plate[6],license_plate[7])
이렇게 한 이유: 위 문제에서 배운대로 방법을 써봤다
해답: license_plate = "24가 2210"; print(license_plate[-4:])

print(변수[시작:끝]) 시작부분에 -를 붙이면 뒤에서 부터 출력

여러 자리를 한번에 출력하는 방법
차이점: 해답이 문장이 더 간결하고 내가 쓴 답은 2 2 1 0 이렇게 한글자씩 떨어져서 나오는 반면, 해답은 2210으로 붙어 나온다 '''

'''23번: "홀짝홀짝홀짝" 문자열에서 '홀'만 출력하세요.
내답: string="홀짝홀짝홀짝";print(string[0],string[2],string[4])
이렇게 생각한 이유: 홀만 골라서 프린트하는 방법을 모르겠어서 손수 하나씩 뽑았다.
해답: string = "홀짝홀짝홀짝";print(string[::2])
변수[시작:끝:오프셋]

차이점: 위와 같이 띄어쓰기 유무, 문장길이 차이다.
'''

'''24번: string = "PYTHON" 문자열을 거꾸로 출력하세요'''
string="PYTHON"; print(string[::-1])

'''25번: phone_number = "010-1111-2222" 하이픈 ('-')을 제거하고 출력하세요.
내답:phone_number = "010-1111-2222"; p1="010 1111 2222"; print(p1)
방법을 아예 모르겠어서 새로운 변수를 선언해 그 안에 값을 넣어주는게 최선이었다.
해답:phone_number = "010-1111-2222"; phone_number1 = phone_number.replace("-", " ") ;print(phone_number1)

변수.replace("제거할 값", "치환할 값")
'''

'''26번: phone_number = "010-1111-2222" 하이픈 ('-')을 제거하고 공백 없이 출력하세요.'''
phone_number = "010-1111-2222"; p1=phone_number.replace("-","");print(p1)

'''27번:  url = "http://sharebook.kr" 도메인을 출력하세요
내답: url = "http://sharebook.kr"; print(url[-2:])
이렇게 생각한 이유: .뒤에있는 부분만 출력하면 되니까 글자수대로 출력해줬다.
해답:url = "http://sharebook.kr";url_split = url.split('.');print(url_split[-1])

변수.split("나누는 기준")

차이점: 내가 프로그래밍한 것은 매번 숫자를 변경해줘야 된다. 
com이면 3으로 kr이면 2로 반면에 해답과 같이 split을 사용하게 된다면 .을 기준으로 나눌 수 있어 간편하게 사용할 수 있다 '''


'''28번:lang = 'python';lang[0] = 'P'; print(lang) 결과를 예상해보세요
내답: P가 출력된다 
해답: 에러가 난다.
이유? 문자열의 경우 수정이 불가능하기때문에 에러가 나는 것이다.'''

'''29번: string = 'abcdfe2a354a32a' a를 A로 변경하세요.'''
 string = 'abcdfe2a354a32a';string.replace("a","A");print(string.replace)

 '''30번: string='abcd';string.replace('b', 'B');print(string) 결과를 예상해보세요
 내답: b가 B로 변경되어 aBcd 가 출력된다.'''