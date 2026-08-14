# 5장 5절 조건을 잇다 — and, or, not

# 셀 1 — 불리언 값 자체를 곧바로 이어 본다
print(True and True)  # True
print(True or False)  # True
print(not True)       # False

# 셀 2 — 비교 연산과 논리 연산의 결합
print((85 >= 60) and (85 <= 100))  # True
print((50 >= 60) or (50 <= 100))   # True
print(not (3 > 5))                 # True

# 셀 3 — 우리가 읽는 순서와 달리 and가 먼저 계산됩니다
print(True or False and False)  # True (True or (False and False))

# 2절의 교훈처럼 의도한 순서를 괄호로 묶어줍니다
age = 20
is_member = False
print((age >= 20) or (is_member and age >= 18))  # True

# 셀 4 — 파이썬은 수학 표기를 그대로 받아 준다: 체이닝
score = 85
print(60 <= score <= 100)  # True

# 셀 5 — 4장에서 배운 교집합과 합집합 연산자입니다 (& | 는 논리 연산자가 아니다)
A = {1, 2, 3}
B = {3, 4, 5}
print(A & B)  # {3}

# 셀 6 — 초보와 AI가 함께 미끄러지는 자리
score = 7
# 에러가 나지 않는 가장 큰 함정입니다
print(score == 3 or 5)  # 5 (truthy — 겉보기엔 통과하지만 의도와 다르다, 진위는 6장)

# 각 비교를 온전한 문장으로 적어야 합니다
print(score == 3 or score == 5)  # False
