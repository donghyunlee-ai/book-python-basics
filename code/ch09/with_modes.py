# ch09-04 잊지 않는 문법과 모드의 계약 — with, r/w/a/x (본문 게재 코드 원본, 5셀 구성)
# 검증 대상(fact-checker 실행 예정): python3
# 산출 파일: hello.txt, log.txt (스크립트 말미에서 삭제)

import os

# 셀 1 — with 블록 첫 사용(자동 close 보장)
with open("hello.txt", "w") as f:
    f.write("이 줄은 with 블록이 씁니다.\n")
# 들여쓰기가 끝났으므로 파일은 이미 안전하게 닫혀 있습니다.

with open("hello.txt", "r") as f:
    print("결과:", f.read())
# 출력: 결과: 이 줄은 with 블록이 씁니다.

# 셀 2 — 'w'는 열기만 해도 파괴적이다(pass로 지나가도 내용이 지워진다)
with open("hello.txt", "w") as f:
    pass

with open("hello.txt", "r") as f:
    print("남은 내용:", f.read())
# 출력: 남은 내용: (빈 문자열)

# 셀 3 — 'a' 모드는 끝에 이어 쓴다(누적)
with open("log.txt", "a") as f:
    f.write("접속 기록이 추가되었습니다.\n")

with open("log.txt", "r") as f:
    print("현재 로그:\n" + f.read())
# 출력: 현재 로그: / 접속 기록이 추가되었습니다.

# 셀 4 — 'x'는 이미 있는 파일이면 거절한다(FileExistsError)
try:
    with open("log.txt", "x") as f:
        f.write("이 코드는 거절당합니다.")
    raise AssertionError("죽어야 하는데 살았음")
except FileExistsError as e:
    last_line = f"FileExistsError: {e!s}"
    print(last_line)
# 출력: FileExistsError: [Errno 17] File exists: 'log.txt'

# 셀 5 — 모드 생략 시 기본값 'r'
# 본문 서술: 셀 3을 두세 번 반복 실행해 로그가 누적된 상태를 가정한다.
# 검증을 위해 여기서 두 번 더 추가해 누적 3줄을 실증한다.
with open("log.txt", "a") as f:
    f.write("접속 기록이 추가되었습니다.\n")
with open("log.txt", "a") as f:
    f.write("접속 기록이 추가되었습니다.\n")

with open("log.txt") as f:  # 모드 생략, 기본값 "r"로 작동
    print("모드 없이 열기:\n" + f.read())
# 출력: 모드 없이 열기: / 접속 기록이 추가되었습니다. (3회 누적)

# 산출 파일 정리(검증 스크립트 전용)
os.remove("hello.txt")
os.remove("log.txt")
