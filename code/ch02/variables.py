# 2장 1절 값에 이름을 붙이다 — 변수
# 출력: 20 / 21 / <class 'int'> / <class 'str'>

# 셀 1 — 할당: age라는 이름표를 값 20에 붙이고 확인
age = 20
print(age)    # 출력: 20

# 셀 2 — 재할당: 오른쪽을 먼저 계산(20 + 1)하고 그 결과에 이름표를 옮겨 붙임
#        노트북에서 이 셀을 Ctrl+Enter로 한 번 더 실행하면 22 — 세션이 최신값을 기억한다는 증거
age = age + 1
print(age)    # 출력: 21

# 셀 3 — type(): 값의 자료형을 알려 주는 함수. type이 돌려준 답을 print에 건네 찍는다
print(type(20))              # 출력: <class 'int'>
print(type("안녕, 파이썬"))   # 출력: <class 'str'>
