# ch03-04 정렬과 요약 — 제자리인가, 새 값인가
# 본문 게재 셀 6개 (python3 실행 검증용 원본)
# 관통 재료 scores는 03절이 [100, 90, 70, 95, 80, 85]로 끝났으므로
# 셀 1·2·3·5에서 원값 [85, 90, 70, 95, 80]을 다시 만든다("표본 다시 만드는 줄").

# --- 셀 1: sort()는 제자리에서 정렬한다
scores = [85, 90, 70, 95, 80]
scores.sort()
print(scores)
# 출력: [70, 80, 85, 90, 95]

# --- 셀 2: 함정 — 재할당하면 리스트를 잃는다
scores = [85, 90, 70, 95, 80]
scores = scores.sort()
print(scores)
# 출력: None

# --- 셀 3: 새 값을 원하면 sorted() — 원본은 무사
scores = [85, 90, 70, 95, 80]
ranked = sorted(scores)
print(ranked)
print(scores)
# 출력: [70, 80, 85, 90, 95]
# 출력: [85, 90, 70, 95, 80]

# --- 셀 4: 같은 이분법의 두 번째 쌍 — [::-1](새 값) vs reverse()(제자리)
print(scores[::-1])
print(scores)
scores.reverse()
print(scores)
# 출력: [80, 95, 70, 90, 85]
# 출력: [85, 90, 70, 95, 80]
# 출력: [80, 95, 70, 90, 85]

# --- 셀 5: 답만 주는 부류 — count와 index
scores = [85, 90, 70, 95, 80]
print(scores.count(85))
print(scores.index(90))
# 출력: 1
# 출력: 1

# --- 셀 6: 리스트를 요약하는 내장 함수 — max/min/sum과 평균
print(max(scores))
print(min(scores))
print(sum(scores))
print(sum(scores) / len(scores))
# 출력: 95
# 출력: 70
# 출력: 420
# 출력: 84.0
