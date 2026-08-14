# 9장 6절 수학 도우미, 결과를 기억하다 — 소수 목록 저장·복원
# 실행하면 primes.txt를 만들고, 마지막에 지웁니다.

import os

# 셀 1 — 2~100 소수 판정·저장, 곧이어 복원
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

with open("primes.txt", "w", encoding="utf-8") as f:
    for n in range(2, 101):
        if is_prime(n):
            f.write(f"{n}\n")

primes = []
with open("primes.txt", "r", encoding="utf-8") as f:
    for line in f:
        primes.append(int(line))

print(f"복원된 소수: {len(primes)}개")
print(f"5번째 소수: {primes[4]}")
# 출력: 복원된 소수: 25개 / 5번째 소수: 11
assert len(primes) == 25
assert primes[4] == 11

# 셀 2 — 101~200 구간을 'a' 모드로 이어 붙이기
with open("primes.txt", "a", encoding="utf-8") as f:
    for n in range(101, 201):
        if is_prime(n):
            f.write(f"{n}\n")

primes_updated = []
with open("primes.txt", "r", encoding="utf-8") as f:
    for line in f:
        primes_updated.append(int(line))

print(f"새로 찾은 소수: {len(primes_updated) - 25}개")
print(f"업데이트된 전체 소수: {len(primes_updated)}개")
# 출력: 새로 찾은 소수: 21개 / 업데이트된 전체 소수: 46개
assert len(primes_updated) == 46
assert len(primes_updated) - 25 == 21

# 실습으로 만든 파일 정리(책에는 없는 단계)
os.remove("primes.txt")
