# ch03-08 연습문제 — 본문 게재 코드 원본 (python3 실행 검증)
# 문항 1: 원형 = 연습문제 1-3 (리스트에 6 추가·1 제거) + 중간고사 2번 유형(pop 반환 혼동) 예방
# 문항 2: 원형 = 중간고사 3번 유형(반환값 미할당)의 리스트판 — 04절 sort None 함정
# 문항 3: 원형 = 07절 코너 오답 코드의 변형 — 05절 별칭, 코너 예고 회수 지점
# 문항 4: 원형 = 연습문제 1-4 (튜플↔리스트 변환 후 요소 추가) + 중간고사 1번(분류 함정) 해설 소재
# 트레이스백 전문 게재 0건 (문항 4 AttributeError는 마지막 줄 인용만) — Colab 대조 목록 추가 없음

# ---- 문항 1 (해설 코드) ----
data = [1, 2, 3, 4, 5]
data.append(6)
data.remove(1)
print(data)             # 본문 해설: [2, 3, 4, 5, 6]
assert data == [2, 3, 4, 5, 6]

print(data.pop())       # 본문 해설: 6
print(data)             # 본문 해설: [2, 3, 4, 5]
assert data == [2, 3, 4, 5]

# ---- 문항 2 (문항 게재 코드) ----
scores = [70, 95, 80]
scores = scores.sort()
print(scores)           # 본문: None
assert scores is None

# 문항 2 해설 — 고치는 길 둘
scores = [70, 95, 80]
scores.sort()           # 길 1: 재할당 없이 제자리 정렬
print(scores)           # [70, 80, 95]
assert scores == [70, 80, 95]

scores = [70, 95, 80]
scores = sorted(scores) # 길 2: 새 리스트를 돌려받아 재할당
print(scores)           # [70, 80, 95]
assert scores == [70, 80, 95]

# ---- 문항 3 (문항 게재 코드) ----
prices = [30, 10, 20]
backup = prices
prices.sort()
print(backup)           # 본문: [10, 20, 30] — 백업까지 정렬됨 (별칭)
assert backup == [10, 20, 30] and backup is prices

# 문항 3 해설 — 수정: copy()로 진짜 복사
prices = [30, 10, 20]
backup = prices.copy()  # 또는 prices[:]
prices.sort()
print(prices)           # [10, 20, 30]
print(backup)           # [30, 10, 20] — 원래 순서 보존
assert prices == [10, 20, 30] and backup == [30, 10, 20]
# [:]도 같은 결과인지 확인 (본문 해설의 괄호 언급 검증)
prices = [30, 10, 20]
backup = prices[:]
prices.sort()
assert backup == [30, 10, 20]

# ---- 문항 4 (문항 게재 코드 — 에러는 마지막 줄 인용만) ----
t = (1, 2, 3, 4, 5)
try:
    t.append(6)
except AttributeError as e:
    last_line = f"{type(e).__name__}: {e}"
    print(last_line)
    # 본문 인용 문구와 실물 대조
    assert last_line == "AttributeError: 'tuple' object has no attribute 'append'"

# 문항 4 해설 — 변환 왕복
t = (1, 2, 3, 4, 5)
temp = list(t)
temp.append(6)
t = tuple(temp)
print(t)                # 본문 해설: (1, 2, 3, 4, 5, 6)
assert t == (1, 2, 3, 4, 5, 6)

print("모든 검증 통과")
