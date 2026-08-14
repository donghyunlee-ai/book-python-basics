# 6장 연습문제
# 아직 배우지 않은 for/while/def/input은 쓰지 않습니다.

# 문항 1 — 성적 등급 판독기 (예측-실행-대조: score = 95 / 72 / 50)
score = 95
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
# 출력: A

score = 72
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
# 출력: C

score = 50
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
# 출력: F

# 문항 1 — 경계값 확인 (score = 90 / 80)
score = 90
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
# 출력: A

score = 80
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
# 출력: B

# 문항 2 — 짝수, 홀수, 그리고 0 (예측형: n = 8 / 7 / 0)
n = 8
if n > 0 and n % 2 == 0:
    print("양의 짝수입니다.")
elif n > 0 and n % 2 != 0:
    print("양의 홀수입니다.")
else:
    print("0이거나 음수입니다.")
# 출력: 양의 짝수입니다.

n = 7
if n > 0 and n % 2 == 0:
    print("양의 짝수입니다.")
elif n > 0 and n % 2 != 0:
    print("양의 홀수입니다.")
else:
    print("0이거나 음수입니다.")
# 출력: 양의 홀수입니다.

n = 0
if n > 0 and n % 2 == 0:
    print("양의 짝수입니다.")
elif n > 0 and n % 2 != 0:
    print("양의 홀수입니다.")
else:
    print("0이거나 음수입니다.")
# 출력: 0이거나 음수입니다.  (n > 0이 이미 거짓 — and 뒤는 확인하지 않음)

# 문항 3 — 이 코드, 어디가 이상할까 (오답: 독립 if 세 개, 3절의 함정)
score = 95
if score >= 90:
    print("A")
if score >= 80:
    print("B")
if score >= 70:
    print("C")
# 출력: A / B / C  (세 줄 전부 — 의도는 A 하나)

# 문항 3 — 수정 코드 (elif 사슬)
score = 95
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
# 출력: A  (한 줄만)

# 문항 4 — 이 코드, 어디가 이상할까 (오답: `or "일"`이 항상 참, 5절의 함정)
day = "월"
if day == "토" or "일":
    print("주말입니다")
else:
    print("평일입니다")
# 출력: 주말입니다  (월요일인데도 — "일" 문자열이 항상 truthy)

# 문항 4 — 수정 코드 (양쪽 비교식을 온전히 명시)
day = "월"
if day == "토" or day == "일":
    print("주말입니다")
else:
    print("평일입니다")
# 출력: 평일입니다

day = "토"
if day == "토" or day == "일":
    print("주말입니다")
else:
    print("평일입니다")
# 출력: 주말입니다
