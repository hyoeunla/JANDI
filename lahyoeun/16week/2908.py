a, b = list(input().split())
a = a[::-1]
b = b[::-1]
a_list = list(map(int, str(a)))
b_list = list(map(int, str(b)))
num_a = a_list[0]*100 + a_list[1]*10 + a_list[2]
num_b = b_list[0]*100 + b_list[1]*10 + b_list[2]
if num_a >= num_b:
    print(num_a)
else:
    print(num_b)
