# 3장 2절 같은 규칙 — 인덱스와 슬라이스 다시
# 책의 셀 순서대로. scores는 01절과 같은 리스트다.

scores = [85, 90, 70, 95, 80]

# --- 셀 1: 인덱스 두 규칙이 그대로 ---
print(scores[0])
print(scores[-1])
print(scores[len(scores) - 1])
# 출력: 85
# 출력: 80
# 출력: 80

# --- 셀 2: 슬라이스도 그대로 — 결과는 새 리스트 ---
print(scores[1:4])
# 출력: [90, 70, 95]

# --- 셀 3: 생략·간격·뒤집기 + 원본 무사 확인 ---
print(scores[2:])
print(scores[::2])
print(scores[::-1])
print(scores)
# 출력: [70, 95, 80]
# 출력: [85, 70, 80]
# 출력: [80, 95, 70, 90, 85]
# 출력: [85, 90, 70, 95, 80]  (원본 그대로 — 슬라이스는 새 리스트)

# --- 셀 4: 에러까지 같다 (에러 마지막 줄만 확인) ---
try:
    print(scores[5])
except IndexError as e:
    print(f"IndexError: {e}")
# 에러 마지막 줄: IndexError: list index out of range

# --- 셀 5: +와 * — 연산자의 뜻은 자료형이 정한다 (세 번째 확인) ---
print([1, 2] + [3, 4])
print([0] * 3)
# 출력: [1, 2, 3, 4]
# 출력: [0, 0, 0]

# --- 셀 6: 리스트 + 숫자는 거절 (에러 마지막 줄만 확인) ---
try:
    print([1, 2] + 3)
except TypeError as e:
    print(f"TypeError: {e}")
# 에러 마지막 줄: TypeError: can only concatenate list (not "int") to list

# --- 셀 7: in — 들어 있는지 묻는다 ---
print(90 in scores)
# 출력: True
