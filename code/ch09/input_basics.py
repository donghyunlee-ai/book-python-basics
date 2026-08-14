# 9장 1절 프로그램에 말 걸기 — input
# 책에서는 input()으로 입력을 받습니다. 여기서는 바로 실행되도록 입력값을 미리 넣어 두었습니다(책의 코드는 주석으로 남겼습니다).

# 셀 1 — 첫 대화
# 책의 코드: name = input("이름을 알려 주세요: ")
name = "파이썬"  # 책에서는 input()으로 입력받는 값
print(f"반갑습니다, {name} 님!")

# 셀 2 — 계산기 코드: "33" 배반
# 책의 코드: a = input("숫자: ")
a = "3"  # 책에서는 input()으로 입력받는 값
print(a + a)
# 출력: 33

# 셀 3 — type(a)로 정체 확인
print(type(a))
# 출력: <class 'str'>

# 셀 4 — int 변환·재할당
# 책의 코드: a = input("숫자: ")
a = "3"  # 책에서는 input()으로 입력받는 값
a = int(a)
print(a + a)
# 출력: 6

# 셀 5 — int(input()) 관용형
# 책의 코드: a = int(input("숫자: "))
a = int("3")  # 책에서는 input()으로 입력받는 값

# 셀 6 — gcd에 입력 연결(함수 본문에는 input을 넣지 않는다)
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 책의 코드: num1 = int(input("첫 번째 숫자: "))
# 책의 코드: num2 = int(input("두 번째 숫자: "))
num1 = int("48")  # 책에서는 input()으로 입력받는 값
num2 = int("36")  # 책에서는 input()으로 입력받는 값

result = gcd(num1, num2)
print(f"두 수의 최대공약수는 {result}입니다.")
# 출력: 두 수의 최대공약수는 12입니다.
assert result == 12
