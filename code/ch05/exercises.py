# ch05-08 연습문제 — 본문 게재 코드 원본 (python3 실행 검증 예정)
# 문항 1: 산술 연산과 우선순위 예측하기 (원형 = 연습문제 2-1·2-5 변주)
# 문항 2: 판정의 결과 예측하기 (원형 = 연습문제 2-2·2-3·2-4 통합 변주)
# 문항 3: 코드 리뷰형 — 정수 나눗셈으로 0이 되는 백분율 (원형 정신: 중간고사 13번)
# 문항 4: 코드 리뷰형 — 소수를 ==로 비교하는 판정 (04절 회수)

# ---- 문항 1 (문항 게재 코드) ----
a = 9
b = 4

print(a + b)  # 13
print(a - b)  # 5
print(a * b)  # 36
print(a / b)  # 2.25
print(a // b)  # 2
print(a % b)  # 1

print(2 ** 3 * 2 - 10 / 5)  # 14.0
assert (a + b, a - b, a * b, a / b, a // b, a % b) == (13, 5, 36, 2.25, 2, 1)
assert 2 ** 3 * 2 - 10 / 5 == 14.0

# ---- 문항 2 (문항 게재 코드) ----
score = 85

print(score >= 90)                       # False
print((score >= 60) and (score < 90))    # True
print(not (score == 85))                 # False
print(60 <= score <= 100)                # True
print(85 in [80, 85, 90])                # True
assert (score >= 90, (score >= 60) and (score < 90), not (score == 85), 60 <= score <= 100, 85 in [80, 85, 90]) == (False, True, False, True, True)

# ---- 문항 3 (문항 게재 코드 — 오답) ----
correct = 7
total = 10
rate = correct // total * 100

print(f"정답률: {rate}%")  # 정답률: 0%
assert rate == 0

# 문항 3 해설 — 올바른 수정
rate_fixed = correct / total * 100
print(f"정답률: {rate_fixed}%")  # 정답률: 70.0%
assert rate_fixed == 70.0

# ---- 문항 4 (문항 게재 코드 — 오답) ----
total_amount = 0.1 + 0.2
print(total_amount == 0.3)  # False
assert (total_amount == 0.3) is False

# 문항 4 해설 — round로 안전하게 비교
print(round(total_amount, 1) == 0.3)  # True
assert (round(total_amount, 1) == 0.3) is True

print("모든 검증 통과")
