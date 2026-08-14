# 10장 2절 만들기 루프가 한 문장으로 — 리스트 컴프리헨션

# [셀 1]
nums = [1, 2, 3, 4, 5]
squares = []
for n in nums:
    squares.append(n * n)
print(squares)
# 출력: [1, 4, 9, 16, 25]

# [셀 2]
squares_comp = [n * n for n in nums]
print(squares_comp)
# 출력: [1, 4, 9, 16, 25]

# [셀 3]
print(squares == squares_comp)
print(nums)
# 출력:
# True
# [1, 2, 3, 4, 5]

# [셀 4]
total = sum([n * n for n in nums])
count = len([n * n for n in nums])
print(f"합계: {total}, 개수: {count}")
# 출력: 합계: 55, 개수: 5

# [셀 5]
lines = ["  apple \n", "banana  ", "\n cherry "]
clean_lines = [line.strip() for line in lines]
print(clean_lines)
# 출력: ['apple', 'banana', 'cherry']
