# 6장 1절 만약에 — if와 들여쓰기
# 출력: 합격입니다 / (셀 2 SyntaxError: expected ':') / (셀 3 IndentationError: expected an
#       indented block after 'if' statement on line 3) / (셀 4 SyntaxError: invalid syntax.
#       Maybe you meant '==' or ':=' instead of '='?) / 안내를 종료합니다.

# 셀 1 — 점수가 85점인 학생의 합격 여부를 if로 판정합니다.
score = 85

if score >= 60:
    print("합격입니다")

print("-" * 20)

# 셀 2 — 조건 끝의 콜론(:)을 빠뜨리면 SyntaxError입니다 (에러는 마지막 줄만 적음, 실행하면
# 아래 셀들이 돌지 않으므로 주석 처리):
# score = 85
#
# if score >= 60
#     print("합격입니다")
#
# SyntaxError: expected ':'

# 셀 3 — 콜론은 있지만 다음 줄에 들여쓰기가 없으면 IndentationError입니다 (주석 처리):
# score = 85
#
# if score >= 60:
# print("합격입니다")
#
# IndentationError: expected an indented block after 'if' statement on line 3

# 셀 4 — 비교(==) 대신 대입(=)을 조건에 쓰면 SyntaxError입니다 (주석 처리):
# score = 60
#
# if score = 60:
#     print("합격입니다")
#
# SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?

# 셀 5 — 조건이 거짓이면 블록 전체를 건너뛰고, 들여쓰기가 끝난 줄부터 다시 실행합니다.
score = 40

if score >= 60:
    print("합격입니다")
    print("축하합니다")

print("안내를 종료합니다.")
