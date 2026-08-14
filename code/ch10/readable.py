# ch10-01 읽기 좋은 코드 — "파이썬답다"의 기준 (본문 게재 코드 원본 — writer 기계적 추출, 미실행)
# 검증 대상(fact-checker 실행 예정): python3

# [셀 1]
# 9장에서 썼던 풀어 쓴 루프 (정확하지만 평범합니다)
lines = ["2\n", "3\n", "5\n"]

primes = []
for line in lines:
    primes.append(int(line))

print(primes)
# 출력: [2, 3, 5]

# [셀 2]
# 이 장에서 배울 알맞은 한 문장 (예고편: 의도가 바로 보입니다)
primes_idiom = [int(line) for line in lines]

print(primes_idiom)
# 출력: [2, 3, 5]

# [셀 3]
# 줄 수만 줄인 욱여넣은 한 줄 (가장 짧지만 읽기 괴롭습니다)
primes_crammed = list(map(int, "".join(lines).split()))

print(primes_crammed)
# 출력: [2, 3, 5]
