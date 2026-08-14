# 4장 5절 집합 연산과 set()
# 예제 원소는 모두 작은 정수라 파이썬 버전과 관계없이 출력이 같다.

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

# --- 더 알아보기: 책의 설명을 직접 확인하는 코드(책에는 없음) ---
# 합·교·차의 원소 구성 자체는 순서와 무관하게 불변
assert A | B == {1, 2, 3, 4, 5, 6}
assert A & B == {3, 4}
assert A - B == {1, 2}
assert B - A == {5, 6}
assert set(numbers) == {1, 2, 3}
assert len(set(ratings)) == 3
assert sorted(set(ratings)) == [3, 4, 5]
