# ch09-08 연습문제 (본문 게재 코드 원본 — 문항 4개 + 해설. input()은 검증용 하드코딩으로 대체)
# 검증 대상(fact-checker 실행 예정): python3
# assert: 문항1 "35"→8, 문항2 개수·합계, 문항3 'w' 한 줄 덮어쓰기(누적 실패)→'a' 정답,
#         문항4 max 사전순 함정("9\n" > "85\n")→int 변환 정답

import os

# ===== 문항 1 — 입력과 변환의 함정 =====
# 본문 원본(문제):
# a = input("첫 번째 숫자를 입력하세요: ")
# b = input("두 번째 숫자를 입력하세요: ")
# print("두 숫자의 합:", a + b)
a = "3"  # 검증용 하드코딩 입력값
b = "5"  # 검증용 하드코딩 입력값
result_wrong = a + b
print("두 숫자의 합(오답):", result_wrong)
assert result_wrong == "35"

# 해설: int로 변환해야 8이 나온다
a2 = int("3")
b2 = int("5")
print("두 숫자의 합(정답):", a2 + b2)
assert a2 + b2 == 8

# ===== 문항 2 — 센티널 입력과 파일 왕복 =====
# 본문 원본은 input()으로 -1이 나올 때까지 반복 입력받지만,
# 검증을 위해 하드코딩된 입력 목록을 순서대로 소비하는 반복으로 대체한다(무한 대기 방지).
_inputs = iter(["10", "20", "30", "-1"])

print("숫자를 입력하세요 (-1을 입력하면 종료합니다).")
with open("records.txt", "w", encoding="utf-8") as f:
    while True:
        user_input = next(_inputs)  # 본문 원본: input("숫자: ")
        if user_input == "-1":
            break
        f.write(user_input + "\n")

count = 0
total_sum = 0
with open("records.txt", "r", encoding="utf-8") as f:
    for line in f:
        count += 1
        total_sum += int(line)

print(f"입력된 숫자는 총 {count}개이고, 합계는 {total_sum}입니다.")
assert count == 3
assert total_sum == 60

# ===== 문항 3 — 이 코드, 어디가 이상할까(w 모드의 파괴성) =====
# 본문 원본(문제 — 오답):
# measurement = input("새 측정 온도를 입력하세요: ")
# with open("temperature.log", "w", encoding="utf-8") as f:
#     f.write(measurement + "\n")
measurement1 = "36.5"  # 검증용 하드코딩 입력값(1회차 실행)
with open("temperature.log", "w", encoding="utf-8") as f:
    f.write(measurement1 + "\n")

measurement2 = "37.1"  # 검증용 하드코딩 입력값(2회차 실행 — 'w'라서 1회차 값이 지워진다)
with open("temperature.log", "w", encoding="utf-8") as f:
    f.write(measurement2 + "\n")

with open("temperature.log", "r", encoding="utf-8") as f:
    lost_content = f.read()
print("오답 결과(직전 값만 남음):", repr(lost_content))
assert lost_content == "37.1\n"

# 해설: 'a' 모드로 누적
os.remove("temperature.log")
measurement1 = "36.5"
with open("temperature.log", "a", encoding="utf-8") as f:
    f.write(measurement1 + "\n")
measurement2 = "37.1"
with open("temperature.log", "a", encoding="utf-8") as f:
    f.write(measurement2 + "\n")

with open("temperature.log", "r", encoding="utf-8") as f:
    kept_content = f.read()
print("정답 결과(누적됨):", repr(kept_content))
assert kept_content == "36.5\n37.1\n"

# ===== 문항 4 — 이 코드, 어디가 이상할까(문자열 max의 사전순 함정) =====
with open("scores.txt", "w", encoding="utf-8") as f:
    f.write("85\n9\n78\n")

with open("scores.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

top_score_wrong = max(lines)
print("최고 점수(오답):", top_score_wrong)
assert top_score_wrong == "9\n"

# 해설: int로 변환한 뒤 비교해야 한다
scores = []
with open("scores.txt", "r", encoding="utf-8") as f:
    for line in f:
        scores.append(int(line))

top_score = max(scores)
print("최고 점수(정답):", top_score)
assert top_score == 85

# 산출 파일 정리(검증 스크립트 전용)
os.remove("records.txt")
os.remove("temperature.log")
os.remove("scores.txt")
