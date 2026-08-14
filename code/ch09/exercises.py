# 9장 8절 연습문제 (문항 4개 + 해설)
# 책에서는 input()으로 입력을 받습니다. 여기서는 바로 실행되도록 입력값을 미리 넣어 두었습니다(책의 코드는 주석으로 남겼습니다).

import os

# ===== 문항 1 — 입력과 변환의 함정 =====
# 책의 문제 코드:
# a = input("첫 번째 숫자를 입력하세요: ")
# b = input("두 번째 숫자를 입력하세요: ")
# print("두 숫자의 합:", a + b)
a = "3"  # 책에서는 input()으로 입력받는 값
b = "5"  # 책에서는 input()으로 입력받는 값
result_wrong = a + b
print("두 숫자의 합(오답):", result_wrong)
assert result_wrong == "35"

# 해설: int로 변환해야 8이 나온다
a2 = int("3")
b2 = int("5")
print("두 숫자의 합(정답):", a2 + b2)
assert a2 + b2 == 8

# ===== 문항 2 — 센티널 입력과 파일 왕복 =====
# 책에서는 input()으로 -1이 나올 때까지 반복 입력받지만,
# 여기서는 미리 넣어 둔 입력 목록을 차례로 쓰도록 바꿨습니다(입력을 기다리며 멈추지 않도록).
_inputs = iter(["10", "20", "30", "-1"])

print("숫자를 입력하세요 (-1을 입력하면 종료합니다).")
with open("records.txt", "w", encoding="utf-8") as f:
    while True:
        user_input = next(_inputs)  # 책의 코드: input("숫자: ")
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
# 책의 문제 코드(오답):
# measurement = input("새 측정 온도를 입력하세요: ")
# with open("temperature.log", "w", encoding="utf-8") as f:
#     f.write(measurement + "\n")
measurement1 = "36.5"  # 책에서는 input()으로 입력받는 값(1회차 실행)
with open("temperature.log", "w", encoding="utf-8") as f:
    f.write(measurement1 + "\n")

measurement2 = "37.1"  # 책에서는 input()으로 입력받는 값(2회차 실행 — 'w'라서 1회차 값이 지워진다)
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

# 실습으로 만든 파일 정리(책에는 없는 단계)
os.remove("records.txt")
os.remove("temperature.log")
os.remove("scores.txt")
