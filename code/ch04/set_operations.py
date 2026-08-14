# ch04-05 집합 연산과 set() — 본문 코드 원본
# 검증: python3(3.14) + anaconda python3.12 교차 실행 — 집합 출력 버전 불변 확인
# 예제 원소는 전부 연속 소정수(해시 충돌 없음) — 「버전 고정」 정책(memory.md) 준수

# 셀 1 — 합·교·차 연산자
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B)   # {1, 2, 3, 4, 5, 6}
print(A & B)   # {3, 4}
print(A - B)   # {1, 2}

# 셀 2 — 차집합의 방향 (예측-실행-대조)
print(B - A)   # {5, 6}

# 셀 3 — set() 변환: 리스트의 중복 제거
numbers = [1, 2, 2, 3, 3, 3]
print(set(numbers))        # {1, 2, 3}

# 셀 4 — 실전 관용구 두 개, 그리고 대가(순서 소실)
ratings = [4, 5, 4, 3, 5, 4]
print(len(set(ratings)))   # 3
print(list(set(ratings)))  # [3, 4, 5] — 응답이 들어온 순서(4가 먼저)가 사라짐

# --- 산문 주장 검증(본문 비게재) ---
# 합·교·차의 원소 구성 자체는 순서와 무관하게 불변
assert A | B == {1, 2, 3, 4, 5, 6}
assert A & B == {3, 4}
assert A - B == {1, 2}
assert B - A == {5, 6}
assert set(numbers) == {1, 2, 3}
assert len(set(ratings)) == 3
assert sorted(set(ratings)) == [3, 4, 5]
