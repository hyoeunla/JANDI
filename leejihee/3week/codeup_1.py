'''
[1]
Hello
출력하기
'''
print("Hello")

'''
[2]
Hello World
출력하기
'''
print("Hello World")

'''
[3]
Hello
World
(두 줄에 걸쳐 줄을 바꿔 출력하기)
'''
# 1)
print("Hello\nWorld")

# 2)
print('''\
Hello
World  
''')

'''
[4]
'Hello'
(단, 작은 따옴표도 함께 출력한다.)
'''
# 1)
print("'Hello'")

# 2)
print('\'Hello\'')

# 3)
print("""'Hello'""")

'''
[5]
"Hello World"
(단, 큰따옴표도 함께 출력한다.)
'''
# 1)
print('"Hello"')

# 2)
print("\"Hello\"")

# 3)
print('''"Hello"''')

'''
[6]
"!@#$%^&*()"
(단, 큰따옴표도 함께 출력한다.)
'''
print('"!@#$%^&*()"')

'''
[7]
"C:\Download\hello.cpp"
(단, 큰따옴표도 함께 출력한다.)
'''
print('"C:\Download\hello.cpp"')

'''
[8]
┌┬┐
├┼┤
└┴┘
출력하기
'''
# 1)
print('''\
┌┬┐
├┼┤
└┴┘
''')

# 2)
print('┌┬┐\n├┼┤\n└┴┘')
