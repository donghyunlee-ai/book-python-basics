# 3장 8절 연습문제
# 문항 1: 리스트에 6 추가·1 제거, pop이 돌려주는 값
# 문항 2: 04절 sort()가 None을 돌려주는 함정
# 문항 3: 07절 [AI와 짝 코딩] 오답 코드의 변형 — 05절 별칭
# 문항 4: 튜플↔리스트 변환 후 요소 추가

# ---- 문항 1 (해설 코드) ----
data = [1, 2, 3, 4, 5]
data.append(6)
data.remove(1)
print(data)             # 출력: [2, 3, 4, 5, 6]
assert data == [2, 3, 4, 5, 6]

print(data.pop())       # 출력: 6
print(data)             # 출력: [2, 3, 4, 5]
assert data == [2, 3, 4, 5]

# ---- 문항 2 (문제 코드) ----
scores = [70, 95, 80]
scores = scores.sort()
print(scores)           # 출력: None
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

# ---- 문항 3 (문제 코드) ----
prices = [30, 10, 20]
backup = prices
prices.sort()
print(backup)           # 출력: [10, 20, 30] — 백업까지 정렬됨 (별칭)
assert backup == [10, 20, 30] and backup is prices

# 문항 3 해설 — 수정: copy()로 진짜 복사
prices = [30, 10, 20]
backup = prices.copy()  # 또는 prices[:]
prices.sort()
print(prices)           # [10, 20, 30]
print(backup)           # [30, 10, 20] — 원래 순서 보존
assert prices == [10, 20, 30] and backup == [30, 10, 20]
# [:]도 같은 결과인지 확인
prices = [30, 10, 20]
backup = prices[:]
prices.sort()
assert backup == [30, 10, 20]

# ---- 문항 4 (문제 코드 — 에러는 마지막 줄만 확인) ----
t = (1, 2, 3, 4, 5)
try:
    t.append(6)
except AttributeError as e:
    last_line = f"{type(e).__name__}: {e}"
    print(last_line)
    # 책에 옮긴 에러 문구와 같은지 확인
    assert last_line == "AttributeError: 'tuple' object has no attribute 'append'"

# 문항 4 해설 — 변환 왕복
t = (1, 2, 3, 4, 5)
temp = list(t)
temp.append(6)
t = tuple(temp)
print(t)                # 출력: (1, 2, 3, 4, 5, 6)
assert t == (1, 2, 3, 4, 5, 6)

print("모든 확인을 통과했습니다")
