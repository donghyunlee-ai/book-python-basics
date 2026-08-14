# 4장 8절 연습문제
# 문항 1: 프로필 딕셔너리 (1절 조회 + 2장 f-string 계산식 + 2절 추가 + len)
# 문항 2: 집합의 합·교·차 — 원소가 모두 8보다 작은 정수라 파이썬 버전과 관계없이 출력이 같다
# 문항 3: 오타 키에 대괄호로 할당하면 수정이 아니라 새 항목이 생긴다 (02절)
# 문항 4: 값을 in으로 딕셔너리에 물으면 항상 False (03절)

# ---- 문항 1 (해설 — 예시 답안) ----
profile = {"이름": "김파이", "태어난 해": 2005}
print(f"안녕하세요, {profile['이름']}입니다. 올해 {2026 - profile['태어난 해']}살이 됩니다.")
# 출력: 안녕하세요, 김파이입니다. 올해 21살이 됩니다.
assert 2026 - profile['태어난 해'] == 21
profile["사는 곳"] = "서울"
print(len(profile))     # 출력: 3 (쌍 2 → 3, 없는 키 할당 = 추가)
assert len(profile) == 3

# ---- 문항 2 (문제 코드) ----
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
print(A | B)            # 출력: {1, 2, 3, 4, 5, 6, 7}
print(A & B)            # 출력: {4, 5}
print(A - B)            # 출력: {1, 2, 3}
print(B - A)            # 출력: {6, 7}
# 출력 모양이 책과 같은지 확인 (repr 문구까지)
assert repr(A | B) == "{1, 2, 3, 4, 5, 6, 7}"
assert repr(A & B) == "{4, 5}"
assert repr(A - B) == "{1, 2, 3}"
assert repr(B - A) == "{6, 7}"

# ---- 문항 3 (문제 코드) ----
scores = {"김파이": 80}
scores["김 파이"] = 95  # 공백 오타 — 수정이 아니라 유령 항목 추가
print(scores)           # 출력: {'김파이': 80, '김 파이': 95}
print(len(scores))      # 출력: 2
assert repr(scores) == "{'김파이': 80, '김 파이': 95}"
assert len(scores) == 2 and scores["김파이"] == 80

# 문항 3 해설 — 올바른 수정 + 확인
scores = {"김파이": 80}
scores["김파이"] = 95
assert scores == {"김파이": 95}
assert len(scores) == 1                      # 해설: len이 1인지 확인
assert list(scores.keys()) == ["김파이"]     # 해설: 이름표가 하나뿐인지 확인 (3절 검증 수단)

# ---- 문항 4 (문제 코드) ----
phone = {"김파이": "010-1234-5678"}
print("010-1234-5678" in phone)              # 출력: False (in은 키만 본다)
assert ("010-1234-5678" in phone) is False

# 문항 4 해설 — 의도대로 고치기
print("010-1234-5678" in phone.values())     # 출력: True
assert ("010-1234-5678" in phone.values()) is True

print("모든 확인을 통과했습니다")
