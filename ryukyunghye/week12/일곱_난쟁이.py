# [2309] 일곱 난쟁이
heights = []
for _ in range(9):
    heights.append(int(input()))
total = sum(heights)
for i in range(9):
    for j in range(i+1, 9):
        if total - (heights[i] + heights[j]) == 100:
            smallPerson1, smallPerson2 = heights[i], heights[j]
            heights.remove(smallPerson1)
            heights.remove(smallPerson2)
            heights.sort()
            for i in range(7):
                print(heights[i])
            break
    if len(heights) == 7:
        break
