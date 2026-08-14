# ch10-05 나란히 걷기 — zip (본문 게재 코드 원본 — writer 기계적 추출, 미실행)
# 검증 대상(fact-checker 실행 예정): python3

# [셀 1]
numbers = [11, 15, 17, 21]
results = [True, False, True, False]

for i in range(len(numbers)):
    n = numbers[i]
    ok = results[i]
    print(f"숫자 {n}의 소수 판정: {ok}")
# 출력:
# 숫자 11의 소수 판정: True
# 숫자 15의 소수 판정: False
# 숫자 17의 소수 판정: True
# 숫자 21의 소수 판정: False

# [셀 2]
numbers = [11, 15, 17, 21]
results = [True, False, True, False]

# zip이 만든 짝짓기 결과를 눈으로 확인하기 위해 list()로 묶습니다.
print(list(zip(numbers, results)))
# 출력: [(11, True), (15, False), (17, True), (21, False)]

# [셀 3]
numbers = [11, 15, 17, 21]
results = [True, False, True, False]

for n, ok in zip(numbers, results):
    print(f"숫자 {n}의 소수 판정: {ok}")
# 출력:
# 숫자 11의 소수 판정: True
# 숫자 15의 소수 판정: False
# 숫자 17의 소수 판정: True
# 숫자 21의 소수 판정: False

# [셀 4]
numbers = [11, 15, 17]                      # 3개뿐입니다.
results = [True, False, True, False, True]  # 5개나 있습니다.

# 3개짜리와 5개짜리 리스트를 zip으로 묶어 봅니다.
print(list(zip(numbers, results)))
# 출력: [(11, True), (15, False), (17, True)]

# [셀 5]
numbers = [11, 15, 17]
results = [True, False, True]
times = ["0.01초", "0.02초", "0.01초"]

for n, ok, time in zip(numbers, results, times):
    print(f"숫자 {n} ({ok}) - 소요 시간: {time}")
# 출력:
# 숫자 11 (True) - 소요 시간: 0.01초
# 숫자 15 (False) - 소요 시간: 0.02초
# 숫자 17 (True) - 소요 시간: 0.01초

# [셀 6]
# 처음부터 튜플로 한 몸처럼 묶어 두는 설계
prime_data = [
    (11, True),
    (15, False),
    (17, True),
    (21, False)
]

for n, ok in prime_data:
    print(f"숫자 {n}의 소수 판정: {ok}")
# 출력:
# 숫자 11의 소수 판정: True
# 숫자 15의 소수 판정: False
# 숫자 17의 소수 판정: True
# 숫자 21의 소수 판정: False
