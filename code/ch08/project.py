# ch08-06 수학 도우미의 부품화 — gcd와 is_prime (본문 게재 코드 원본 — writer 기계적 추출, 미실행)
# 검증 대상(fact-checker 실행 예정): python3
# fact-checker 중점 검증: gcd 정확판(+1 경계)·lcm·is_prime 경계(1, 2)·5번째 소수

# [셀 1] 절차를 함수로 감싼다 — 정확판 gcd (경계값 min(a,b)까지 포함하도록 +1)
def gcd(a, b):
    answer = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            answer = i
    return answer

print(gcd(12, 6))
print(gcd(48, 36))
# 출력:
# 6
# 12

# [셀 2] lcm은 gcd를 부품으로 쓴다
def lcm(a, b):
    return a * b // gcd(a, b)

print(lcm(12, 6))
print(lcm(15, 10))
# 출력:
# 12
# 30

# [셀 3] is_prime — 판정을 True/False로 반환 (조기 반환, 경계값 1·2 확인)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(9))
print(is_prime(2))
print(is_prime(1))
# 출력:
# True
# False
# True
# False

# [셀 4] 부품을 조립해 쓴다
# 4-1. 2부터 100 사이의 소수 나열하기
for n in range(2, 101):
    if is_prime(n):
        print(n, end=" ")
print()

# 4-2. 5번째 소수 찾기 (while True + n += 1로 증가하므로 반드시 종료된다)
count = 0
n = 2
while True:
    if is_prime(n):
        count += 1
        if count == 5:
            print(f"5번째 소수: {n}")
            break
    n += 1
# 출력:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
# 5번째 소수: 11
