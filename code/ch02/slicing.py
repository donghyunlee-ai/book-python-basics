# 2장 4절 인덱스와 슬라이스 — 문자열 해부하기
# 출력: 11 / H W / d / d H / (셀 5는 IndexError) / Hello / _World
#       / Hello World Hello_World / HloWrd dlroW_olleH Hello_World

# 셀 1 — 해부 표본 준비. 밑줄도 한 글자라 길이는 11 (03절 "길이 세는 눈" 복습)
s = "Hello_World"
print(len(s))       # 출력: 11

# 셀 2 — 인덱스는 0부터: "몇 번째 칸"이 아니라 "시작점에서 몇 칸 갔는가"
print(s[0])         # 출력: H (첫 글자 = 0칸 간 곳)
print(s[6])         # 출력: W (사람 셈 여섯 번째는 _ 이지만, 6칸 가면 W)

# 셀 3 — 마지막 인덱스 = len(s) - 1 = 10 ("하나 어긋남"의 발원지)
print(s[10])        # 출력: d

# 셀 4 — 음수 인덱스는 뒤에서 세기. s[10]과 s[-1]은 같은 칸
print(s[-1])        # 출력: d (끝 글자 관용구)
print(s[-11])       # 출력: H

# 셀 5 — 범위 밖은 IndexError. 새 세션에서 셀 1~5 순차 실행 시 In[5]
# IPython 트레이스백 실물 (가운데 줄은 환경·실행 이력에 따라 다를 수 있음, 마지막 줄은 불변):
#   ---------------------------------------------------------------------------
#   IndexError                                Traceback (most recent call last)
#   Cell In[5], line 1
#   ----> 1 print(s[11])
#
#   IndexError: string index out of range
# print(s[11])      # 실행하면 위 에러 — 아래 셀들이 돌도록 주석 처리

# 셀 6 — 슬라이스 s[시작:끝]: 시작 포함, 끝 미포함. 글자 수 = 끝 - 시작
print(s[0:5])       # 출력: Hello (인덱스 5의 _ 는 미포함)

# 셀 7 — 같은 번호에서 끝나고 시작하면 겹침도 빈틈도 없이 이어진다 (눈금 모델)
print(s[5:11])      # 출력: _World

# 셀 8 — 생략 = "되는 데까지"
print(s[:5])        # 출력: Hello (처음부터)
print(s[6:])        # 출력: World (끝까지 — 뒷 단어 관용구)
print(s[:])         # 출력: Hello_World (전부)

# 셀 9 — 세 번째 자리 = 간격. [::-1]은 뒤집기 관용구 (08절 연습문제 문항 4에서 다시 나온다)
print(s[::2])       # 출력: HloWrd
print(s[::-1])      # 출력: dlroW_olleH
print(s)            # 출력: Hello_World — 슬라이스는 원본을 바꾸지 않고 새 문자열을 돌려준다
