# ch04-07 [AI와 짝 코딩] 코너 — 오답 코드·해설 주장 검증 (python3)
# 본문 게재 코드 블록 1개 + 해설 문장 단위 실물 대조

# --- 본문 오답 코드 블록 (AI가 돌려주기 쉬운 코드 — 예시 데이터에선 성공) ---
scores = {"김파이": 90, "이코드": 85}
print(scores["김파이"])  # 본문 서술: "실행하면 90이 잘 나옵니다"
assert scores["김파이"] == 90

# --- 해설: 예시 밖 이름을 넣는 순간 죽는다 (마지막 줄만 본문 인용) ---
try:
    scores["김코드"]
    raise AssertionError("죽어야 하는데 살았음")
except KeyError as e:
    last_line = f"KeyError: {e!s}"
    print(last_line)
    assert last_line == "KeyError: '김코드'"  # 본문 인용 문구와 일치

# --- 좋은 요청의 기대 출력 쌍: 김파이 → 90, 김코드 → 미등록 ---
assert scores.get("김파이", "미등록") == 90
assert scores.get("김코드", "미등록") == "미등록"
print(scores.get("김코드", "미등록"))

# --- 의심 ②: 기본값 0은 "0점 학생"과 "미등록"을 구분하지 못한다 ---
scores2 = {"김파이": 90, "박튜플": 0}          # 박튜플은 실제 0점
assert scores2.get("박튜플", 0) == scores2.get("김코드", 0) == 0  # 구분 불가 실증

# --- 검증 수단: list(d.keys())·in (3절 도구) ---
print(list(scores.keys()))                      # ['김파이', '이코드']
assert list(scores.keys()) == ["김파이", "이코드"]
assert ("김코드" in scores) is False

print("corner.py: 전 검증 통과")
