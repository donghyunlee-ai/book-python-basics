# 5장 1절 나눗셈의 두 얼굴 — 몫과 나머지

# 셀 1 — 나눗셈(/)의 결과는 나누어떨어져도 항상 float
print(6 / 2)
print(8 / 4)

# 셀 2 — 정수 몫(//)과 나머지(%), 그리고 검산
print(17 // 5)
print(17 % 5)
print(5 * 3 + 2)
print(17.0 // 5)  # float가 한 방울 섞이면 결과도 float

# 셀 3 — 범인 검거: 1장의 평균 오답 코드 재현과 수정
scores = [4, 3, 5, 2]
# 1장의 오답 코드 재현
print("평균 점수:", sum(scores) // len(scores))

# 범인을 지목하고 수정한 코드
print("평균 점수:", sum(scores) / len(scores))

# 셀 4 — 음수 나눗셈: //(내림) vs int()(절사)
print(-7 // 2)
print(int(-3.5))

# 셀 5 — %의 쓸모: 홀짝 판정과 자릿수 분해
print(10 % 2)
print(7 % 2)
print(379 % 10)
print(379 // 10)

# 셀 6 — 0으로 나누기는 거절당한다 (ZeroDivisionError, 에러 메시지는 마지막 줄만 출력)
try:
    print(10 / 0)
    raise AssertionError("예상과 다름: 에러가 나야 하는데 실행이 계속됨")
except ZeroDivisionError as e:
    last_line = f"ZeroDivisionError: {e!s}"
    print(last_line)
    assert last_line == "ZeroDivisionError: division by zero"
