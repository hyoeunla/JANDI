# 일곱 난쟁이

import random
dwarf = []
dwarf_7 = []
result = 0
for i in range(9):
    dwarf.append(int(input()))

while 1:
    if (result == 100 and len(dwarf_7) == 7):
        break
    else:
        result = 0
        dwarf_7 = []
        for i in range(7):
            choice_7 = random.choice(dwarf)
            if choice_7 in dwarf_7:
                choice_7 = random.choice(dwarf)
            else:
                dwarf_7.append(choice_7)
        result = sum(dwarf_7)
dwarf_7.sort()
for i in dwarf_7:
    print(i)
