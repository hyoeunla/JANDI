'''
171번: 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
price_list = [32100, 32150, 32000, 32500]

32100
32150
32000
32500
'''
price_list = [32100, 32150, 32000, 32500]

for i in range(4):
    print(price_list[i])

'''
172번: 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
price_list = [32100, 32150, 32000, 32500]

0 32100
1 32150
2 32000
3 32500
'''
price_list = [32100, 32150, 32000, 32500]

for i in range(4):
    print(i, price_list[i])

'''
173번: 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
price_list = [32100, 32150, 32000, 32500]

3 32100
2 32150
1 32000
0 32500
'''
price_list = [32100, 32150, 32000, 32500]

for i in range(3, -1, -1):
    print(i, price_list[3-i])

'''
다른방법
'''
price_list = [32100, 32150, 32000, 32500]

for i in range(len(price_list)):
    print((len(price_list) - 1) - i, price_list[i])

'''
174번: 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
price_list = [32100, 32150, 32000, 32500]

100 32150
110 32000
120 32500
'''
price_list = [32100, 32150, 32000, 32500]
a = 1
for i in range(100, 130, 10):
    print(i, price_list[a])
    a += 1

'''
다른 방법
'''
for i in range(1, 4):
    print(90 + 10 * i, price_list[i])

'''
175번: my_list를 아래와 같이 출력하라.
my_list = ["가", "나", "다", "라"]

가 나
나 다
다 라
'''
my_list = ["가", "나", "다", "라"]
for i in range(0, 4):
    if i+1 < 4:
        print(my_list[i], my_list[i+1])

'''
다른 방법 1
'''
for i in range(len(my_list) - 1):
    print(my_list[i], my_list[i+1])

'''
다른 방법 2
'''
for i in range(1, len(my_list)):
    print(my_list[i-1], my_list[i])

'''
176번:리스트를 아래와 같이 출력하라.
my_list = ["가", "나", "다", "라", "마"]
가 나 다
나 다 라
다 라 마
'''
my_list = ["가", "나", "다", "라", "마"]
for i in range(len(my_list)-2):
    print(my_list[i], my_list[i+1], my_list[i+2])

'''
다른방법
'''
for i in range(1, len(my_list) - 1):
    print(my_list[i-1], my_list[i], my_list[i+1])

'''
다른방법
'''
for i in range(2, len(my_list)):
    print(my_list[i-2], my_list[i-1], my_list[i])


'''
177번: 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하라.
my_list = ["가", "나", "다", "라"]
라 다
다 나
나 가
'''
my_list = ["가", "나", "다", "라"]
for i in range(3, 0, -1):
    print(my_list[i], my_list[i-1])


'''
178번: 리스트에는 네 개의 정수가 저장되어 있다. 각각의 데이터에 대해서 자신과 우측값과의 차분값을 화면에 출력하라.
my_list = [100, 200, 400, 800]
100
200
400
'''
my_list = [100, 200, 400, 800]
for i in range(0, 3):
    print(my_list[i+1] - my_list[i])

'''
179번: 리스트에는 6일 간의 종가 데이터가 저장되어 있다. 종가 데이터의 3일 이동 평균을 계산하고 이를 화면에 출력하라.
233.33333333333334
466.6666666666667
733.3333333333334
1033.3333333333333
my_list = [100, 200, 400, 800, 1000, 1300]
'''
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(0, 4):
    print((my_list[i]+my_list[i+1]+my_list[i+2])/3)

'''
다른방법
'''
for i in range(1, len(my_list) - 1):
    print(abs(my_list[i-1] + my_list[i] + my_list[i+1]) / 3)

'''
180번: 리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 
고가와 저가의 차를 변동폭이라고 정의할 때, low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
'''
low_prices = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(high_prices)):
    volatility.append(high_prices[i] - low_prices[i])
