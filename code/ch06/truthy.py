# 6장 5절 참인 것과 거짓인 것 — 참·거짓의 폭

# 셀 1 — 리스트·정수를 조건 자리에 직접 두면 파이썬이 나름의 참·거짓 기준으로 판정합니다.
scores = [85, 90, 70]
if scores:
    print("목록에 점수가 있습니다.")

empty_scores = []
if empty_scores:
    print("이 문장은 출력되지 않습니다.")

if 5:
    print("5는 참 대접을 받습니다.")

if 0:
    print("0은 참일까요?")
else:
    print("0은 거짓 대접을 받습니다.")

print("-" * 20)

# 셀 2 — if len(scores) > 0: 대신 if scores: 로 짧게 쓰는 파이썬다운 관용구.
scores = [85, 90]

# 초보자의 길고 명시적인 표기
if len(scores) > 0:
    print(f"최고 점수: {max(scores)}")

# 파이썬다운 짧은 관용구
if scores:
    print(f"최고 점수: {max(scores)}")

print("-" * 20)

# 셀 3 — 함정: `score == 3 or 5`는 `(score == 3) or 5`로 끊어 읽혀 5(참)가 항상 이깁니다.
score = 2

# 함정: 에러 없이 언제나 참이 되어 실행됩니다.
if score == 3 or 5:
    print("이 문장은 무조건 출력됩니다.")

# 올바른 표기: 조건이 거짓이므로 실행되지 않습니다.
if score == 3 or score == 5:
    print("3점이거나 5점입니다.")
else:
    print("점수가 3이나 5가 아닙니다.")

print("-" * 20)

# 셀 4 — or/and는 True/False가 아니라 승패를 결정한 값 자체를 돌려줍니다.
print(3 or 5)
print(0 or 5)

print("-" * 20)

# 셀 5 — `x or 기본값` 관용구: 값이 있으면 그 값, 없으면 기본값.
print("" or "익명")
print("홍길동" or "익명")

print("-" * 20)

# 셀 6 — 단락 평가: 왼쪽이 거짓이면 오른쪽은 아예 실행되지 않습니다(0으로 나누기 회피).
x = 0

# 왼쪽(x != 0)이 거짓이므로 오른쪽(10 / x > 1)은 아예 실행되지 않습니다.
if x != 0 and 10 / x > 1:
    print("계산 성공")
else:
    print("0으로 나눌 수 없어 안전하게 건너뛰었습니다.")
