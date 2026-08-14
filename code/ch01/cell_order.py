# 1장 3절 노트북 사용의 최소 원리 — 셀 실행 순서
#
# 노트북에서는 아래 두 줄이 각각 별도의 셀이다.
#   [셀 1] a = 3
#   [셀 2] print(a)
#
# 실행 순서 실험:
#   (1) 새 세션에서 셀 2만 먼저 실행 → NameError. 에러여도 실행 번호는 부여됨: 셀 2 = In[1]
#       (트레이스백의 "Cell In[1]"과 일치)
#       ---------------------------------------------------------------------------
#       NameError                                 Traceback (most recent call last)
#       Cell In[1], line 1
#       ----> 1 print(a)
#
#       NameError: name 'a' is not defined
#   (2) 셀 1 실행(In[2]) 후 셀 2 재실행(In[3]) → 3
#       → 이 시점 화면: 위 셀 [2], 아래 셀 [3]

a = 3       # 셀 1
print(a)    # 셀 2 — 정순 실행 시 출력: 3
# 참고: 트레이스백 머리 형식은 환경마다 다르다 — 로컬 IPython 9.x는 'Cell In[1], line 1',
# Colab에서는 '/tmp/ipython-input-*.py in <cell line: 0>()' 형식으로 보일 수 있다.
# 마지막 줄(NameError: name 'a' is not defined)은 어디서나 같다.
