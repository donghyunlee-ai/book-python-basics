# 7장 3절 쌓아 가기 — 누적 변수와 회차별 추적 표

# [셀 1]
total = 0
for i in range(1, 101):
    total += i

print(total)
# 출력: 5050

# [셀 2]
count = 0
for n in range(1, 101):
    if n % 3 == 0:
        count += 1

print(count)
# 출력: 33

# [셀 3]
evens = []
for n in range(1, 11):
    if n % 2 == 0:
        evens.append(n)

print(evens)
# 출력: [2, 4, 6, 8, 10]

# [셀 4]
odds_squared = []
for n in range(1, 11):
    if n % 2 == 1:
        odds_squared.append(n * n)

print(odds_squared)
# 출력: [1, 9, 25, 49, 81]

# [셀 5]
scores = [85, 90, 70, 95, 80]
biggest = scores[0]

for score in scores:
    if score > biggest:
        biggest = score

print(biggest)
# 출력: 95

