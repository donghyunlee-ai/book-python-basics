# 11장 2절 설계도 그리기 — class, __init__, self

# [셀 1] 첫 설계도와 실물 만들기 — class와 type()
class BankAccountV1:
    pass

# 클래스 이름을 함수처럼 호출하면 새로운 실물이 태어납니다.
account_a = BankAccountV1()
account_b = BankAccountV1()

# 타입(자료형)을 확인해 보면 우리가 만든 BankAccountV1이라고 나옵니다.
print(type(account_a))
# 출력: <class '__main__.BankAccountV1'>

# [셀 2] 태어나는 순간의 약속: __init__
class BankAccountV2:
    def __init__(self, name):
        # 실물이 태어나는 순간 자동으로 실행되며 인자를 받습니다.
        print(f"새 계좌 개설 준비: 예금주 {name}")

# 호출할 때 건넨 "김파이"가 __init__의 name으로 들어갑니다.
a2 = BankAccountV2("김파이")
# 출력: 새 계좌 개설 준비: 예금주 김파이

# [셀 3] 속성: 실물의 칸 채우기
class BankAccountV3:
    def __init__(self, name):
        # 왼쪽의 self.name은 '실물의 칸'
        # 오른쪽의 name은 괄호로 건네받은 '매개변수'입니다.
        self.name = name
        self.balance = 0  # 잔액은 항상 0으로 시작합니다.

a3 = BankAccountV3("김파이")
print(f"예금주: {a3.name}")
print(f"첫 잔액: {a3.balance}원")
# 출력: 예금주: 김파이
# 출력: 첫 잔액: 0원

# [셀 4] 매개변수의 죽음과 속성의 생존
class BankAccountV4:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        # __init__ 실행이 끝나면 매개변수 name은 소멸합니다.

a4 = BankAccountV4("김파이")

# 실물의 칸(속성)에 담긴 값은 무사히 살아남아 출력됩니다.
print(a4.name)
# 출력: 김파이

# 책에 실린 형태(주석을 풀고 실행하면 NameError가 발생합니다):
# print(name)
#
# 확인용: NameError가 실제로 나는지 확인합니다
try:
    print(name)  # noqa: F821 (의도적으로 정의되지 않은 이름)
except NameError as e:
    print(f"NameError: {e}")

# [셀 5] 이 장의 최대 고비: self의 실체 증명 — a.deposit(5000)과 BankAccount.deposit(a, 5000)은 등가
class BankAccountV5:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount

a5 = BankAccountV5("김파이")

# 1. 우리가 쓰는 보통의 방식 (파이썬이 a를 숨겨서 전달)
a5.deposit(5000)
print(a5.balance)
# 출력: 5000

# 2. 파이썬이 내부적으로 이해하는 실제 방식 (완전히 같은 동작)
BankAccountV5.deposit(a5, 5000)
print(a5.balance)
# 출력: 10000

# [셀 6] 격리와 상태: 실물마다 자기 값을 가진다
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount

a6 = BankAccount("김파이")
b6 = BankAccount("이코드")

# a 계좌에만 5000원 입금
a6.deposit(5000)

# 두 실물은 서로 철저히 격리되어 각자의 값을 기억합니다.
print(f"{a6.name}의 잔액: {a6.balance}")
print(f"{b6.name}의 잔액: {b6.balance}")
# 출력: 김파이의 잔액: 5000
# 출력: 이코드의 잔액: 0

assert a5.balance == 10000
assert a6.balance == 5000
assert b6.balance == 0
