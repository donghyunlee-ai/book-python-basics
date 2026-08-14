# ch01-03 노트북 사용의 최소 원리 — 셀 실행 순서 시연 (2셀 구성)
#
# 노트북에서는 아래 두 줄이 각각 별도의 셀이다.
#   [셀 1] a = 3
#   [셀 2] print(a)
#
# 시연 시나리오 (python3 + IPython InteractiveShell, store_history=True로 검증, 2026-07-06):
#   (1) 새 세션에서 셀 2만 먼저 실행 → NameError. 에러여도 실행 번호는 부여됨: 셀 2 = In[1]
#       (트레이스백의 "Cell In[1]"과 일치)
#       ---------------------------------------------------------------------------
#       NameError                                 Traceback (most recent call last)
#       Cell In[1], line 1
#       ----> 1 print(a)
#
#       NameError: name 'a' is not defined
#   (2) 셀 1 실행(In[2]) 후 셀 2 재실행(In[3]) → 3
#       → 이 시점 화면: 위 셀 [2], 아래 셀 [3] (본문 서술과 일치해야 함)

a = 3       # 셀 1
print(a)    # 셀 2 — 정순 실행 시 출력: 3
# 주의: 트레이스백 머리 형식은 환경별로 다름 — 로컬 IPython 9.x는 'Cell In[1], line 1',
# 현행 Colab(IPython 7.34 고정)은 '/tmp/ipython-input-*.py in <cell line: 0>()' 형식.
# 마지막 줄(NameError: name 'a' is not defined)은 불변. 조판 전 Colab 라이브 1회 대조(typesetter 항목).
