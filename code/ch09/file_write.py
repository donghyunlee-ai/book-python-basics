# 9장 2절 파일에 쓰다 — open, write, close
# 실행하면 hello.txt를 만들고, 마지막에 지웁니다.

import os

# 셀 1 — 쓰기 모드로 새 파일을 열고, 손잡이 f에 할당
f = open("hello.txt", "w")
print(type(f))
# 출력: <class '_io.TextIOWrapper'>

# 셀 2 — print 습관대로 두 번 쓰면 줄이 바뀔까요? (배반: 줄바꿈 없이 붙는다)
f.write("안녕, 파이썬.")
f.write("반갑습니다.")

# 셀 3 — 줄을 바꾸려면 \n을 직접 써야 한다. write()의 반환값(쓴 글자 수)도 확인
message = "이제 줄이 바뀝니다."
length = f.write(f"\n{message}\n")
print("쓴 글자 수:", length)
# 출력: 쓴 글자 수: 13
assert length == 13

# 셀 4 — 다 썼다면 반드시 닫는다
f.close()

# 셀 5 — 같은 세션에서 읽기 모드로 다시 열어 확인
f2 = open("hello.txt", "r")
text = f2.read()
print(text)
f2.close()
assert text == "안녕, 파이썬.반갑습니다.\n이제 줄이 바뀝니다.\n"

# 실습으로 만든 파일 정리(책에는 없는 단계)
os.remove("hello.txt")
