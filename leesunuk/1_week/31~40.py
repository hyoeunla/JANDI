'''31번: a = "3"; b = "4"; print(a + b) 결과를 예상해보세요.
내답: 34
'''

'''32번: print("Hi"*3) 결과를 예상해보세요.
내답: HiHiHi
'''

'''33번: 화면에 '-'를 80개 출력하세요.
내답: a='-';b=a*80;print(b)
다른 방법: print("-" * 80)
'''

'''34번: t1 = 'python' t2 = 'java' 위와 같이 문자열이 바인딩 되어 있을때 변수에 문자열 더하기와 곱하기를 사용해 
python java python java python java python java 와같이 출력해보세요
내답: t1 = 'python'; t2 = 'java'; print((t1+' '+t2+' ')*3)
다른 방법:  t1 = "python";t2 = "java";t3 = t1 + ' ' + t2 + ' ';print(t3 * 4)
'''

'''35번: name1 = "김민수" age1 = 10 name2 = "이철희" age2 = 13 와 같이 바인딩 되어 있을때
% formatting을 사용해서 다음과 같이 출력해보세요.

 내답: name1 = "김민수"; age1 = 10; name2 = "이철희"; age2 = 13
 print("이름:",name1,"나이:",age1);print("이름:",name2,"나이:",age2)
 
 해답: name1 = "김민수"; age1 = 10; name2 = "이철희"; age2 = 13
print("이름: %s 나이: %d" % name1, age1);print("이름: %s 나이: %d" % name2, age2)

차이점: 내답은 포맷팅을 사용하지 못해서 결과값은 같으나 문제는 틀렸다. '''

'''36번: format() 메서드를 사용해 35번 문제를 풀어보세요"

내답: name1 = "김민수"; age1 = 10; name2 = "이철희"; age2 = 13
a=format(%d, age1);b=format(%d, 2); print("이름:", a, "나이:", b)

해답: name1 = "김민수"; age1 = 10; name2 = "이철희"; age2 = 13
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

차이점: 사용해본 적이 없는 메서드라 생각나는대로 해봤는데 에러가 났다..'''

'''37번: 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.
name1 = "김민수"; age1 = 10; name2 = "이철희"; age2 = 13
print(f"이름: {name1} 나이: {age1}");print(f"이름: {name2} 나이: {age2}")

푼방법: 완전 처음 보는 건데 계속 내 생각만으로 풀순 없으니까 네이버에 사용하는 방법 즉 형식을 보고 그거에 맞춰서 풀어봤다 '''

'''38번:삼성전자의 상장주식수("5,969,782,550")가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.

내답: sj='5,969,782,550'; sj1=int(sj.replace(",","")); print(sj1, type(sj1))

다른 방법: 상장주식수 = "5,969,782,550"; 컴마제거 = 상장주식수.replace(",", ""); 타입변환 = int(컴마제거) ;print(타입변환, type(타입변환)) '''

'''39번: 분기 = "2020/03(E) (IFRS연결)"에서 '2020/03'만 출력하세요.'''
분기 = "2020/03(E) (IFRS연결)"; print(분기[0:7])

'''data = "   삼성전자    " 좌우의 공백을 제거해보세요.
내답: data = "   삼성전자    "; d=data.replace(" ","");print(d)

다른 방법: data = "   삼성전자    ";data1 = data.strip(); print(data1)

변수.strip() <--공백 제거 메서드'''