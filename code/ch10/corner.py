# 10장 7절 [AI와 짝 코딩] "파이썬답게 바꿔줘" — 읽기 어려운 한 줄은 개선이 아니다

# [셀 1] 오답 코드 — 모르는 부품(all, 중첩 for)이 든 압축된 한 줄
primes = [n for n in range(2, 101) if all(n % d != 0 for d in range(2, n))]
print(len(primes))
# 출력: 25 (동작 자체는 맞지만 이 절의 기준으로는 "모르는 부품이 든 한 줄"이라 채택하지 않습니다)

# [셀 2] 좋은 답 코드 — 6절에서 만든 형태 그대로 (읽는 사람이 아는 문법 안에서 판별 논리를 함수로 분리)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primes = [n for n in range(2, 101) if is_prime(n)]
print(len(primes))
# 출력: 25
