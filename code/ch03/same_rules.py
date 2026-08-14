# ch03-02 같은 규칙 — 인덱스와 슬라이스 다시
# 본문 셀 순서대로. python3로 실행 검증.
# scores 재료는 01절과 동일 (장 관통 재료 — 수치 변경 금지).

scores = [85, 90, 70, 95, 80]

# --- 셀 1: 인덱스 두 규칙이 그대로 ---
print(scores[0])
print(scores[-1])
print(scores[len(scores) - 1])
# 검증 출력: 85
# 검증 출력: 80
# 검증 출력: 80

# --- 셀 2: 슬라이스도 그대로 — 결과는 새 리스트 ---
print(scores[1:4])
# 검증 출력: [90, 70, 95]

# --- 셀 3: 생략·간격·뒤집기 + 원본 무사 확인 ---
print(scores[2:])
print(scores[::2])
print(scores[::-1])
print(scores)
# 검증 출력: [70, 95, 80]
# 검증 출력: [85, 70, 80]
# 검증 출력: [80, 95, 70, 90, 85]
# 검증 출력: [85, 90, 70, 95, 80]  (원본 그대로 — 슬라이스는 새 리스트)

# --- 셀 4: 에러까지 같다 (본문에는 마지막 줄만 인용) ---
try:
    print(scores[5])
except IndexError as e:
    print(f"IndexError: {e}")
# 검증(마지막 줄): IndexError: list index out of range

# --- 셀 5: +와 * — 연산자의 뜻은 자료형이 정한다 (세 번째 확인) ---
print([1, 2] + [3, 4])
print([0] * 3)
# 검증 출력: [1, 2, 3, 4]
# 검증 출력: [0, 0, 0]

# --- 셀 6: 리스트 + 숫자는 거절 (본문에는 마지막 줄만 인용) ---
try:
    print([1, 2] + 3)
except TypeError as e:
    print(f"TypeError: {e}")
# 검증(마지막 줄): TypeError: can only concatenate list (not "int") to list

# --- 셀 7: in — 들어 있는지 묻는다 (장 규율: 한 예제만) ---
print(90 in scores)
# 검증 출력: True
