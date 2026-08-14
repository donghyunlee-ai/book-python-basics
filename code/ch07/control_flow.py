# ch07-05 흐름 바꾸기 — break, continue, pass (본문 게재 코드 원본 — writer 기계적 추출, 미실행)
# 검증 대상(fact-checker 실행 예정): python3

# [셀 1]
for i in range(1, 100):
    if i % 7 == 0:
        print(f"첫 번째 7의 배수: {i}")
        break
# 출력: 첫 번째 7의 배수: 7

# [셀 2]
n = 1
while True:
    if n % 11 == 0 and n % 13 == 0:
        print(f"11과 13의 첫 공배수: {n}")
        break
    n += 1
# 출력: 11과 13의 첫 공배수: 143

# [셀 3]
for i in range(1, 12):
    if i % 2 == 0:
        continue
    print(i, end=" ")
# 출력: 1 3 5 7 9 11 

# [셀 4]
print("--- break ---")
for i in range(1, 12):
    if i % 3 == 0:
        break
    print(i, end=" ")
# 출력: --- break ---
# 출력: 1 2 

# [셀 5]
print("--- continue ---")
for i in range(1, 12):
    if i % 3 == 0:
        continue
    print(i, end=" ")
# 출력: --- continue ---
# 출력: 1 2 4 5 7 8 10 11 

# [셀 6]
print("--- pass ---")
for i in range(1, 12):
    if i % 3 == 0:
        pass
    print(i, end=" ")
# 출력: --- pass ---
# 출력: 1 2 3 4 5 6 7 8 9 10 11 

