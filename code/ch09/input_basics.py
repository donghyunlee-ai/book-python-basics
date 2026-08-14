# ch09-01 프로그램에 말 걸기 — input (본문 게재 코드 원본, 6셀 구성 — writer 기계적 추출)
# 검증 대상(fact-checker 실행 예정): python3
# input()은 검증 편의를 위해 하드코딩 값으로 대체(본문 원본은 주석으로 보존)
# 출력 예상: 인사말 / "33"(문자열 이어붙이기) / <class 'str'> / 6(정수 변환) / gcd(48,36)=12

# 셀 1 — 첫 대화
# 본문 원본: name = input("이름을 알려 주세요: ")
name = "파이썬"  # 검증용 하드코딩 입력값
print(f"반갑습니다, {name} 님!")

# 셀 2 — 계산기 코드: "33" 배반
# 본문 원본: a = input("숫자: ")
a = "3"  # 검증용 하드코딩 입력값
print(a + a)
# 출력: 33

# 셀 3 — type(a)로 정체 확인
print(type(a))
# 출력: <class 'str'>

# 셀 4 — int 변환·재할당
# 본문 원본: a = input("숫자: ")
a = "3"  # 검증용 하드코딩 입력값
a = int(a)
print(a + a)
# 출력: 6

# 셀 5 — int(input()) 관용형
# 본문 원본: a = int(input("숫자: "))
a = int("3")  # 검증용 하드코딩 입력값

# 셀 6 — gcd에 입력 연결(함수 본문에는 input을 넣지 않는다)
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 본문 원본: num1 = int(input("첫 번째 숫자: "))
# 본문 원본: num2 = int(input("두 번째 숫자: "))
num1 = int("48")  # 검증용 하드코딩 입력값
num2 = int("36")  # 검증용 하드코딩 입력값

result = gcd(num1, num2)
print(f"두 수의 최대공약수는 {result}입니다.")
# 출력: 두 수의 최대공약수는 12입니다.
assert result == 12
