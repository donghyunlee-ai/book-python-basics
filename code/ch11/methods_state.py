# 11장 3절 상태를 바꾸는 메서드 — 입금과 출금

# [셀 1] deposit — 제자리에서 바꾸는 도구 (검증 없는 최초판)
class BankAccountBasic:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name}: {amount}원 입금 (잔액: {self.balance}원)")

a1 = BankAccountBasic("김파이")
a1.deposit(10000)
a1.deposit(5000)
# 출력: 김파이: 10000원 입금 (잔액: 10000원)
# 출력: 김파이: 5000원 입금 (잔액: 15000원)

# [셀 2] 검증하며 바꾼다 — 조기 반환과 경계값(deposit·withdraw 완성판)
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            print("입금 거절: 0원 이하는 입금할 수 없습니다.")
            return
        self.balance += amount
        print(f"{self.name}: {amount}원 입금 (잔액: {self.balance}원)")

    def withdraw(self, amount):
        if amount <= 0:
            print("출금 거절: 0원 이하는 출금할 수 없습니다.")
            return
        if amount > self.balance:
            print(f"출금 거절: 잔액이 부족합니다. (현재 잔액: {self.balance}원)")
            return
        self.balance -= amount
        print(f"{self.name}: {amount}원 출금 (잔액: {self.balance}원)")

    def get_balance(self):
        return self.balance

a2 = BankAccount("김파이")
a2.deposit(10000)

# [셀 3] withdraw 경계값 — 잔액과 정확히 같은 금액을 출금(전액 인출)하면 성공해야 한다
a2.withdraw(10000)
# 출력: 김파이: 10000원 출금 (잔액: 0원)

# [셀 4] 상태 추적 읽기 — 호출 열을 따라가며 balance 변화를 예측-실행-대조
a3 = BankAccount("김파이")
a3.deposit(10000)
a3.deposit(5000)
a3.withdraw(3000)
a3.withdraw(20000)
# 출력: 김파이: 10000원 입금 (잔액: 10000원)
# 출력: 김파이: 5000원 입금 (잔액: 15000원)
# 출력: 김파이: 3000원 출금 (잔액: 12000원)
# 출력: 출금 거절: 잔액이 부족합니다. (현재 잔액: 12000원)

# [셀 5] get_balance — 답만 주는 도구
a4 = BankAccount("김파이")
a4.deposit(10000)
a4.deposit(5000)
current = a4.get_balance()
print(f"현재 잔액 조회: {current}원")
# 출력: 김파이: 10000원 입금 (잔액: 10000원)
# 출력: 김파이: 5000원 입금 (잔액: 15000원)
# 출력: 현재 잔액 조회: 15000원

# [셀 6] 두 계좌는 서로를 모른다 — 명확해진 주어
a5 = BankAccount("김파이")
a5.deposit(10000)
b5 = BankAccount("이코드")
b5.deposit(500)

a5.deposit(5000)
b5.withdraw(100)

print(f"{a5.name}의 잔액: {a5.get_balance()}원")
print(f"{b5.name}의 잔액: {b5.get_balance()}원")
# 출력: 김파이: 10000원 입금 (잔액: 10000원)
# 출력: 이코드: 500원 입금 (잔액: 500원)
# 출력: 김파이: 5000원 입금 (잔액: 15000원)
# 출력: 이코드: 100원 출금 (잔액: 400원)
# 출력: 김파이의 잔액: 15000원
# 출력: 이코드의 잔액: 400원

assert a2.balance == 0
assert a3.balance == 12000
assert a4.balance == 15000
assert a5.balance == 15000 and b5.balance == 400
