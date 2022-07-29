# 2309. 일곱 난쟁이
dwarf = []
for i in range(9):
    dwarf.append(int(input()))
# 한 줄로 가능: dwarf = [int(input()) for _ in range(9)]

for i in range(8):  # ([0]+[1]) ([0]+[2]) ([0]+[3]) ... ([7]+[8])
    for j in range(i+1, 9):
        if sum(dwarf)-(dwarf[i]+dwarf[j]) == 100:
            a = dwarf[i]  # 15 값이 저장되므로 remove로 삭제
            b = dwarf[j]  # 25
dwarf.remove(a)
dwarf.remove(b)

# join 메서드는 문자열끼리 이어주기 때문에 문자열로 바꿔야 함
# map(함수, 리스트/튜플)
print('\n'.join(map(str, sorted(dwarf))))
