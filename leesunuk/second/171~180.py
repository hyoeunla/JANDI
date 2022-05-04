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
