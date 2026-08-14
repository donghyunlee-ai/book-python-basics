# ch05-03 판정의 언어 — 비교 연산자와 불리언 (본문 게재 코드 원본, 5셀 구성)
# 검증 대상(fact-checker 실행 예정): python3
# 출력 예상: True/True/False/False/False/True | <class 'bool'> | True | True/False/True/True/False | True | 1/2

# 셀 1 — 비교 연산자 6종 (7과 5)
print(7 > 5)
print(7 >= 5)
print(7 < 5)
print(7 <= 5)
print(7 == 5)
print(7 != 5)

# 셀 2 — True/False의 정체: 불리언(bool)
print(type(True))  # <class 'bool'>

# 셀 3 — 판정도 값이므로 이름표를 붙일 수 있다
passed = 85 >= 60
print(passed)  # True

# 셀 4 — ==는 값이 같은지를 묻는다 (자료형별 판정 대비)
print(2 == 2.0)          # True
print("2" == 2)          # False
print("파이썬" == "파이썬")  # True
print([1, 2] == [1, 2])  # True
print([1, 2] == [2, 1])  # False

# 셀 5 — 같은 값과 같은 그릇은 다른 질문이다
a = [1, 2]
b = [1, 2]
print(a == b)  # True (내용물만 같으면 True — 그릇의 동일성은 묻지 않는다)

# 셀 6 — 누적을 줄여 쓰는 표기: +=
count = 0
count = count + 1
print(count)  # 1

count += 1
print(count)  # 2
