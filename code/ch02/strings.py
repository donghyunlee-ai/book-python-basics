# ch02-03 문자열 — 글자를 담는 그릇 (노트북 셀 기준 원본, 6셀 구성)
# 검증: python3 3.14.4 + IPython InteractiveShell 9.12.0 (2026-07-07)
# 출력: 파이썬 / 파이썬 / It's mine / <class 'str'> / 파이썬 / ========== / 7
#       + 셀 5는 TypeError (마지막 줄: can only concatenate str (not "int") to str)

# 셀 1 — 작은따옴표와 큰따옴표는 등가 (책은 큰따옴표 기본)
print("파이썬")     # 출력: 파이썬
print('파이썬')     # 출력: 파이썬

# 셀 2 — 글 안에 따옴표를 넣으려면 다른 쪽 따옴표로 포장
print("It's mine")  # 출력: It's mine
# 같은 쪽 포장 print('It's mine') 은 SyntaxError: unterminated string literal (본문은 "에러가 난다"까지만 서술)

# 셀 3 — 따옴표가 붙으면 생김새가 숫자여도 글 (ch01-06 문항 2 "2+3"의 정식 명명)
print(type("123"))  # 출력: <class 'str'>

# 셀 4 — 문자열의 + 는 연결, * 는 반복 ("연산자의 뜻은 값의 자료형이 정한다")
print("파" + "이썬")   # 출력: 파이썬
print("=" * 10)        # 출력: ==========

# 셀 5 — 문자열 + 숫자는 TypeError (05절 f-string·06절 변환의 동기)
# IPython 트레이스백 실물 (가운데 줄은 환경에 따라 다를 수 있음, 마지막 줄은 불변):
#   ---------------------------------------------------------------------------
#   TypeError                                 Traceback (most recent call last)
#   Cell In[1], line 1
#   ----> 1 print("나이: " + 20)
#
#   TypeError: can only concatenate str (not "int") to str
# print("나이: " + 20)   # 실행하면 위 에러 — 아래 셀 6이 돌도록 주석 처리

# 셀 6 — len: 공백도 쉼표도 한 글자 (예측 6으로 빗나가기 좋은 지점)
print(len("안녕, 파이썬"))  # 출력: 7

# 본문 인라인 언급 — 빈 문자열: 길이 0, 자료형은 str
print(len(""))  # 출력: 0
