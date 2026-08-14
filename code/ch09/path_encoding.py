# ch09-05 어디에 있고, 어떻게 적혔나 — 경로와 인코딩 (본문 게재 코드 원본, 3셀 구성)
# 검증 대상(fact-checker 실행 예정): python3
# 산출 파일: message.txt (스크립트 말미에서 삭제). data/primes.txt는 의도적으로 생성 실패(폴더 없음).

import os

# 셀 1 — 없는 폴더 아래에 파일 쓰기 시도 → FileNotFoundError
try:
    with open("data/primes.txt", "w") as f:
        f.write("2\n3\n5")
    raise AssertionError("죽어야 하는데 살았음")
except FileNotFoundError as e:
    last_line = f"FileNotFoundError: {e!s}"
    print(last_line)
# 출력: FileNotFoundError: [Errno 2] No such file or directory: 'data/primes.txt'

# 셀 2 — 인코딩 불일치: cp949로 쓰고 utf-8로 읽기 → UnicodeDecodeError
with open("message.txt", "w", encoding="cp949") as f:
    f.write("파이썬다움")

try:
    with open("message.txt", "r", encoding="utf-8") as f:
        text = f.read()
    raise AssertionError("죽어야 하는데 살았음")
except UnicodeDecodeError as e:
    print(f"UnicodeDecodeError: {e!s}")
# 출력: UnicodeDecodeError: 'utf-8' codec can't decode byte ...

# 셀 3 — encoding 명시로 왕복 정상화
with open("message.txt", "w", encoding="utf-8") as f:
    f.write("파이썬다움")

with open("message.txt", "r", encoding="utf-8") as f:
    text = f.read()
print(text)
# 출력: 파이썬다움
assert text == "파이썬다움"

# 산출 파일 정리(검증 스크립트 전용)
os.remove("message.txt")
