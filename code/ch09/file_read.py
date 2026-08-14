# 9장 3절 파일을 읽다 — read와 줄 순회
# 실행하면 scores.txt를 만들고, 마지막에 지웁니다.

import os

# 셀 0 — 실습 재료 파일 scores.txt 준비
f = open("scores.txt", "w")
f.write("85\n90\n70\n")
f.close()

# 셀 1 — read() 통짜
f = open("scores.txt", "r")
content = f.read()
f.close()
print(repr(content))
# 출력: '85\n90\n70\n'
assert content == "85\n90\n70\n"

# 셀 2 — print(content)의 두 얼굴
print(content)
# 출력: 85 / 90 / 70 (줄바꿈이 그대로 반영됨)

# 셀 3 — readlines()
f = open("scores.txt", "r")
lines = f.readlines()
f.close()
print(lines)
# 출력: ['85\n', '90\n', '70\n']
assert lines == ["85\n", "90\n", "70\n"]

# 셀 4 — for line in f: 순회(줄마다 빈 줄이 겹친다)
f = open("scores.txt", "r")
for line in f:
    print(line)
f.close()
# 출력: 85 / (빈 줄) / 90 / (빈 줄) / 70 / (빈 줄)

# 셀 5 — 꼬리표 \n의 배반과 strip()
print("5\n" == "5")
s = "5\n"
s = s.strip()
print(s == "5")
# 출력: False / True

# 셀 6 — strip()으로 꼬리표를 떼어 낸 뒤 순회
f = open("scores.txt", "r")
for line in f:
    line = line.strip()
    print(line)
f.close()
# 출력: 85 / 90 / 70

# 셀 7 — 문자열 + 정수는 TypeError (책에서도 주석으로만 보여 줍니다)
line = "5\n"
# line + 1 을 시도하면 아래의 에러가 찍힙니다.
# TypeError: can only concatenate str (not "int") to str

# 셀 8 — int() 변환으로 합산
total = 0
f = open("scores.txt", "r")
for line in f:
    score = int(line)
    total = total + score
f.close()
print(total)
# 출력: 245
assert total == 245

# 셀 9 — 없는 파일을 읽으면 FileNotFoundError (책에서는 주석 예시, 여기서는 직접 실행해 확인)
try:
    open("없는파일.txt", "r")
    raise AssertionError("예상과 다름: 에러가 나야 하는데 실행이 계속됨")
except FileNotFoundError as e:
    last_line = f"FileNotFoundError: {e!s}"
    print(last_line)
# 출력: FileNotFoundError: [Errno 2] No such file or directory: '없는파일.txt'

# 실습으로 만든 파일 정리(책에는 없는 단계)
os.remove("scores.txt")
