# 6장 4절 경계에서 갈린다 — 경계값과 겹치는 조건

# 셀 1 — 60점인 사람의 운명이 등호 하나로 갈립니다.
score = 60

print(">= 60 일 때:")
if score >= 60:
    print("합격")
else:
    print("불합격")

print("> 60 일 때:")
if score > 60:
    print("합격")
else:
    print("불합격")

print("-" * 20)

# 셀 2 — 경계값 60과 그 양옆인 59, 61을 직접 할당하여 경계의 동작을 검증합니다.
score = 59
print(f"{score}점 합격 여부: {score >= 60}")

score = 60
print(f"{score}점 합격 여부: {score >= 60}")

score = 61
print(f"{score}점 합격 여부: {score >= 60}")

print("-" * 20)

# 셀 3 — 60점 이상 90점 미만이라는 두 경계를 체이닝으로 묶어 검사합니다.
# 경계 포함 여부(<=, <)에 주의하세요.
score = 90

if 60 <= score < 90:
    print("B등급입니다.")
else:
    print("B등급이 아닙니다.")

print("-" * 20)

# 셀 4 — 정수 경계만 생각하여 조건을 짜면 소수점 점수에서 틈새에 빠집니다.
score = 79.5

if score >= 80:
    print("A등급")
elif score <= 79:
    print("B등급 이하")
else:
    print("등급 판정 불가")  # 79.5점이 조용히 이곳으로 떨어집니다.

print("-" * 20)

# 셀 5 — 바깥 블록이 자기 일을 따로 하고 있다면 and로 펼칠 때 출력이 달라질 수 있습니다.
score = 80

# 5-1. 들여쓰기가 깊어지는 중첩 if
if score >= 60:
    print("합격입니다.")
    # 안쪽 조건은 바깥 조건이 참일 때만 실행됩니다.
    if score >= 90:
        print("장학금 대상자입니다.")

print("-" * 20)

# 5-2. and를 써서 한 줄로 납작하게 펼친 조건
if score >= 60 and score >= 90:
    print("합격이면서 장학금 대상자입니다.")
