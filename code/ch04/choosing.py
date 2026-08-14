# 4장 6절 네 그릇의 지도
# 문자열 집합은 출력 순서가 보장되지 않으므로 만들기만 하고 출력하지 않는다.

# 셀 1 — 같은 시험, 네 그릇: 생성 + 제출 건수 vs 응시 인원 대조
submissions = ["김파이", "이코드", "박튜플", "김파이"]
exam = ("파이썬 기초", 100)
scores = {"김파이": 95, "이코드": 88, "박튜플": 90}
takers = set(submissions)
print(len(submissions))   # 4
print(len(takers))        # 3

# 셀 2 — 그릇마다 묻는 법이 다르다: 위치 / 자리 / 이름표 / 있느냐
print(submissions[0])     # 김파이
print(exam[1])            # 100
print(scores["김파이"])   # 95
print("박튜플" in takers)  # True

# --- 더 알아보기: 책의 설명을 직접 확인하는 코드(책에는 없음) ---
# takers의 원소 구성은 순서와 무관하게 불변 — 중복 김파이(재제출)가 걸러져 3명
assert takers == {"김파이", "이코드", "박튜플"}
assert len(submissions) == 4 and len(takers) == 3
# 책의 표 4-1 "변경" 열 확인: 리스트·딕셔너리·집합은 고칠 수 있고 튜플은 거절
submissions.append("최집합")
scores["최집합"] = 70
takers.add("최집합")
try:
    exam[0] = "데이터 기초"
    raise SystemExit("예상과 다름: 튜플이 항목 할당을 받아들임")
except TypeError as e:
    assert "does not support item assignment" in str(e)
