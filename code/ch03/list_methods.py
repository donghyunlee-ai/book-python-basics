# 3장 3절 리스트를 바꾸다 — 메서드라는 새 도구
# scores는 셀 1에서 [85, 90, 70, 95, 80]으로 새로 만든 뒤 차례로 고쳐 나간다.

# ── 셀 1: 칸 고쳐 쓰기
scores = [85, 90, 70, 95, 80]
scores[0] = 100
print(scores)
# 기대: [100, 90, 70, 95, 80]

# ── 셀 2: append — 점 표기·메서드 첫 등장
scores.append(85)
print(scores)
# 기대: [100, 90, 70, 95, 80, 85]

# ── 셀 3: 빈 리스트에서 쌓기 (01절의 빈 리스트 todo를 다시 쓴다)
todo = []
todo.append("우유 사기")
todo.append("과제 제출")
print(todo)
# 기대: ['우유 사기', '과제 제출']

# ── 셀 4: insert — 눈금 지정 끼워 넣기
scores.insert(1, 88)
print(scores)
# 기대: [100, 88, 90, 70, 95, 80, 85]

# ── 셀 5: remove — 값으로 지우기
scores.remove(88)
print(scores)
# 기대: [100, 90, 70, 95, 80, 85]

# ── 셀 6: remove는 첫 번째 것만
nums = [5, 3, 5]
nums.remove(5)
print(nums)
# 기대: [3, 5]

# ── 셀 7: pop 반환 대조
data = [10, 30, 50]
print(data.pop())
print(data)
# 기대: 50
#       [10, 30]

# ── 셀 8: pop(인덱스) — 자리를 지정해 꺼내기
print(data.pop(0))
print(data)
# 기대: 10
#       [30]

# --- 더 알아보기: 책의 설명을 직접 확인하는 코드(책에는 없음) ---
# 범위 밖 할당은 거절 — 다섯 칸짜리 scores에 scores[5] = 85 → 범위 밖 거절과 같은 계열의 에러
try:
    check = [85, 90, 70, 95, 80]
    check[5] = 85
except IndexError as e:
    print("(더 알아보기) IndexError:", e)
# 기대: (더 알아보기) IndexError: list assignment index out of range
