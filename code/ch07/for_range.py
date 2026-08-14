# 7장 1절 되풀이 — for와 range

# [셀 1]
for i in [1, 2, 3]:
    print(i)
# 출력: 1
# 출력: 2
# 출력: 3

# [셀 2]
for i in range(1, 6):
    print(i)
# 출력: 1
# 출력: 2
# 출력: 3
# 출력: 4
# 출력: 5

# [셀 3]
for i in range(5):
    print(i)
# 출력: 0
# 출력: 1
# 출력: 2
# 출력: 3
# 출력: 4

# [셀 4]
print(range(1, 6))
# 출력: range(1, 6)

# [셀 5]
print(list(range(1, 6)))
# 출력: [1, 2, 3, 4, 5]

# [셀 6]
print(list(range(1, 11, 2)))
# 출력: [1, 3, 5, 7, 9]

# [셀 7]
for i in range(0, 11, 2):
    print(i)
# 출력: 0
# 출력: 2
# 출력: 4
# 출력: 6
# 출력: 8
# 출력: 10

# [셀 8]
for char in "Python":
    print(char)
# 출력: P
# 출력: y
# 출력: t
# 출력: h
# 출력: o
# 출력: n

