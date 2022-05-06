'''
181번: 아래 표에서 하나의 행을 하나의 리스트로, 총 3개의 리스트를 갖는 이차원 리스트 apart를 정의하라.

101호	102호
201호	202호
301호	302호
'''
apart = [["101호", "102호"], ["201호", "202호"], ["301호", "302호"]]
print(apart)

'''
182번: 아래 표에서 하나의 열을 하나의 리스트로, 총 2개의 리스트를 갖는 이차원 리스트 stock을 정의하라.

시가	종가
100	    80
200	    210
300	    330
'''
stock = [["시가", "100", "200", "300"], ["종가", "80", "210", "330"]]
print(stock)

'''
183번: 아래 표를 stock 이름의 딕셔너리로 표현하라.시가를 key로 저장하고, 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다.
종가 역시 key로 저장하고 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다.


시가	종가
100     80
200	    210
300	    330
'''
stock = {"시가": ["100", "200", "300"], "종가": ["80", "210", "330"]}
print(stock['시가'])
print(stock['종가'])


'''
184번: 아래 표를 stock 이라는 이름의 딕셔너리로 표현하라.
 날짜를 key로 저장하고, 나머지 같은 행의 데이터를 리스트로 저장해서 value로 저장한다. 첫 열이 날짜이다.


10/10	80	110	70	90
10/11	210	230	190	200
'''
stock = {"10/10": ["80", "110", "70", "90"],
         "10/11": ["210", "230", "190", "200"]}
print(stock['10/10'])
print(stock['10/11'])

'''
185번: 리스트에 저장된 데이터를 아래와 같이 출력하라. apart = [ [101, 102], [201, 202], [301, 302] ]
101 호
102 호
201 호
202 호
301 호
302 호
'''
apart = [[101, 102], [201, 202], [301, 302]]
for i in range(3):
    for j in range(2):
        print(apart[i][j], "호")

'''
다른 방법
'''
for row in apart:
    for col in row:
        print(col, "호")

'''
186번: 리스트에 저장된 데이터를 아래와 같이 출력하라. apart = [ [101, 102], [201, 202], [301, 302] ]

301 호
302 호
201 호
202 호
101 호
102 호
'''
apart = [[101, 102], [201, 202], [301, 302]]
for i in apart[2::-1]:
    for j in i:
        print(j, "호")

'''
187번: 리스트에 저장된 데이터를 아래와 같이 출력하라. apart = [ [101, 102], [201, 202], [301, 302] ]

302 호
301 호
202 호
201 호
102 호
101 호
'''
apart = [[101, 102], [201, 202], [301, 302]]
for i in apart[2::-1]:
    for j in i[::-1]:
        print(j, "호")

'''
188번:  리스트에 저장된 데이터를 아래와 같이 출력하라. apart = [ [101, 102], [201, 202], [301, 302] ]

101 호
-----
102 호
-----
201 호
-----
202 호
-----
301 호
-----
302 호
-----
'''
apart = [[101, 102], [201, 202], [301, 302]]
for i in apart:
    for j in i:
        print(j, "호")
        print("-----")


'''
189번:  리스트에 저장된 데이터를 아래와 같이 출력하라. apart = [ [101, 102], [201, 202], [301, 302] ]
101 호
102 호
-----
201 호
202 호
-----
301 호
302 호
-----
'''
apart = [[101, 102], [201, 202], [301, 302]]
for i in apart:
    for j in i:
        print(j, "호")
    print("-----")

'''
190번: 리스트에 저장된 데이터를 아래와 같이 출력하라. apart = [ [101, 102], [201, 202], [301, 302] ]

101 호
102 호
201 호
202 호
301 호
302 호
-----
'''
apart = [[101, 102], [201, 202], [301, 302]]
for i in apart:
    for j in i:
        print(j, "호")
print("-----")