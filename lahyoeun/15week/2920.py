music = [1, 2, 3, 4, 5, 6, 7, 8]
in_music = list(map(int, input().split()))
if music == in_music:
    print("ascending")
elif music == in_music[::-1]:
    print("descending")
else:
    print("mixed")
