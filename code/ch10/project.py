# 10장 6절 수학 도우미를 다듬다 — 컴프리헨션·zip 실전

import os

# [셀 1]
# 1단계 (7장의 방식): 중첩 루프와 조기 탈출 플래그로 억지로 구워낸 코드입니다.
primes_v1 = []
for n in range(2, 101):
    is_p = True
    for i in range(2, n):
        if n % i == 0:
            is_p = False
            break
    if is_p:
        primes_v1.append(n)

# 2단계 (8장의 방식): 판정 논리를 함수 is_prime으로 분리했습니다.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primes_v2 = []
for n in range(2, 101):
    if is_prime(n):
        primes_v2.append(n)

# 3단계 (10장의 기준): 컴프리헨션 한 문장으로 압축합니다.
primes_v3 = [n for n in range(2, 101) if is_prime(n)]

# 세 방식이 모두 똑같은 결과를 내는지 고정값으로 검증합니다.
assert primes_v1 == primes_v2 == primes_v3
primes = primes_v3  # 이후 실습을 위해 이름을 넘겨둡니다.
assert len(primes) == 25
assert primes[4] == 11
print(f"2부터 100까지 소수 개수: {len(primes)}개")
# 출력: 2부터 100까지 소수 개수: 25개

# [셀 2]
numbers = [10, 11, 12, 13, 14]

# 1단계: 판정 결과만 모은 리스트를 컴프리헨션으로 뽑아냅니다.
results = [is_prime(n) for n in numbers]

# 2단계: zip으로 두 그릇을 묶고, 삼항 표현식으로 다듬어 출력합니다.
print("--- 판정 결과 ---")
for n, ok in zip(numbers, results):
    label = "소수" if ok else "합성수"
    print(f"{n}은(는) {label}입니다.")

# 3단계: enumerate를 써서 소수 목록에 1번부터 명시적으로 번호를 매깁니다.
print("\n--- 소수 목록 ---")
# 결과가 너무 길어지지 않게 5개만 끊어서 출력합니다.
for i, p in enumerate(primes[:5], 1):
    print(f"{i}번 소수: {p}")
# 출력:
# --- 판정 결과 ---
# 10은(는) 합성수입니다.
# 11은(는) 소수입니다.
# 12은(는) 합성수입니다.
# 13은(는) 소수입니다.
# 14은(는) 합성수입니다.
#
# --- 소수 목록 ---
# 1번 소수: 2
# 2번 소수: 3
# 3번 소수: 5
# 4번 소수: 7
# 5번 소수: 11

# [셀 3]
# 준비: 9장의 관례를 따라 소수 목록을 텍스트 파일로 안전하게 저장합니다.
with open("primes.txt", "w", encoding="utf-8") as f:
    for p in primes:
        f.write(f"{p}\n")

# 9장의 방식: 3줄에 걸쳐 빈 리스트에 순서대로 복원하는 과정입니다.
primes_old_way = []
with open("primes.txt", "r", encoding="utf-8") as f:
    for line in f:
        primes_old_way.append(int(line))

# 10장의 방식: 파일 객체 f를 컴프리헨션의 그릇으로 삼아 한 줄로 복원합니다.
with open("primes.txt", "r", encoding="utf-8") as f:
    primes_new_way = [int(line) for line in f]

# 두 결과가 완벽히 일치하는지 증명합니다.
assert primes_old_way == primes_new_way
print(f"파일에서 {len(primes_new_way)}개의 소수를 복원했습니다.")
print(primes_old_way == primes_new_way)
# 출력:
# 파일에서 25개의 소수를 복원했습니다.
# True

# 정리: 실습 코드가 만든 파일을 지웁니다(책에는 없는 단계).
os.remove("primes.txt")

# [셀 4]
def is_prime_fast(n):
    if n < 2:
        return False
    # 약수는 짝을 이루므로 제곱근까지만 검사하면 연산량이 크게 줄어듭니다.
    # 단, 끝 미포함 규칙 때문에 경계의 +1을 반드시 붙여야 합니다.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 7장의 교훈: 4와 9 같은 제곱수가 조용히 통과하는지 경계를 지독하게 의심합니다.
assert is_prime_fast(4) == False
assert is_prime_fast(9) == False

# 2~100 전수 검사로 두 판정 논리가 100% 동치임을 증명합니다.
for n in range(2, 101):
    assert is_prime(n) == is_prime_fast(n)

print("개선된 빠른 함수가 2~100 구간 전수 조사에서 기존 함수와 완전히 일치합니다.")
# 출력: 개선된 빠른 함수가 2~100 구간 전수 조사에서 기존 함수와 완전히 일치합니다.
