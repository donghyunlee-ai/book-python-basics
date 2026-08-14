# ch07-02 그릇을 훑다 — 문자열·리스트·딕셔너리 순회 (본문 게재 코드 원본 — writer 기계적 추출, 미실행)
# 검증 대상(fact-checker 실행 예정): python3

# [셀 1]
# 3장에서 만들었던 시험 점수 리스트입니다.
scores = [85, 90, 70, 95, 80]

# for가 리스트의 항목을 하나씩 꺼내 score에 담아 줍니다.
for score in scores:
    print(f"점수: {score}")

# [셀 2]
scores = [85, 90, 70, 95, 80]

# len(scores)는 5이므로, range(5)가 되어 0부터 4까지 순회합니다.
for i in range(len(scores)):
    print(f"{i}번째 칸의 점수: {scores[i]}")

# [셀 3]
# 문자열도 글자들의 '열'이므로 for로 하나씩 꺼낼 수 있습니다.
word = "파이썬"
for ch in word:
    print(f"글자: {ch}")

# [셀 4]
# 4장에서 만들었던 전화번호부 딕셔너리입니다.
phone = {"김파이": "010-1234-5678", "이코드": "010-9876-5432"}

print("--- 키 순회 ---")
for key in phone:
    print(f"이름: {key}")

print("--- 값 순회 ---")
# 값만 필요할 때는 values()를 순회합니다.
for value in phone.values():
    print(f"번호: {value}")

print("--- items 언패킹 순회 ---")
# items()가 돌려주는 튜플을 두 개의 이름표로 곧바로 풀어냅니다.
for key, value in phone.items():
    print(f"{key}의 번호는 {value}입니다.")

# [셀 5]
scores = [85, 90, 70, 95, 80]

# 점수를 5점씩 올리고 싶어서 꺼낸 값을 고쳐 봅니다.
for score in scores:
    score = score + 5  # 꺼낸 이름표를 새 값으로 옮겨 붙일 뿐입니다.

# 원본 리스트를 확인해 보면 하나도 변하지 않았습니다.
print("원본 리스트:", scores)

