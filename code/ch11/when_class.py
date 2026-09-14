# 11장 5절 클래스가 필요한 순간 — 상태가 설계를 정당화한다

# [셀 1] 클래스가 불편해지는 순간: 상태 없는 묶음 — 껍데기만 클래스인 과잉 설계
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

# 굳이 인스턴스를 만들어야 쓸 수 있습니다.
calc = Calculator()
print(calc.add(10, 5))
# 출력: 15

# [셀 2] 단순한 함수 두 개 — 명료한 설계(같은 결과, 더 가벼운 비용)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# 이름만 부르면 즉시 답을 줍니다.
print(add(10, 5))
# 출력: 15

# [셀 3] 가짜 상태와 진짜 상태 구별하기 — GcdLcm은 호출 사이에 변하지 않는 '인자 배달'일 뿐
class GcdLcm:
    def __init__(self, num1, num2):
        # 가짜 상태: 호출 사이에 결코 변하지 않는 값
        self.num1 = num1
        self.num2 = num2

    def gcd(self):
        a, b = self.num1, self.num2
        answer = 1
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                answer = i
        return answer

    def lcm(self):
        return (self.num1 * self.num2) // self.gcd()

# 한 번 넣은 12와 18은 이후로 달라지지 않습니다.
math_tool = GcdLcm(12, 18)
print(math_tool.gcd())
# 출력: 6

# [셀 4] 상속: 남의 코드를 읽는 표지판 — 부모 BankAccount(02~04절에서 완성한 것)와 자식 SavingsAccount
# 앞서 만든 은행 계좌 설계도 (부모)
class BankAccount:
    def __init__(self, account_num, name, balance):
        self.account_num = account_num
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("입금액은 0보다 커야 합니다.")
            return
        self.balance += amount

    def __str__(self):
        return f"Account: {self.account_num}, Name: {self.name}, Balance: {self.balance:.1f}"

# 괄호 안에 부모 이름을 적어 물려받습니다 (자식)
class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        # 잔액에 이자를 더하는 자식만의 새 동작
        interest = self.balance * rate
        self.deposit(interest)

# 자식 설계도로 계좌를 만듭니다.
my_account = SavingsAccount("123456789", "김파이", 10000)

# deposit과 __str__은 부모에게서 물려받아 잘 작동합니다.
my_account.deposit(5000)
my_account.add_interest(0.05)
print(my_account)
# 출력: Account: 123456789, Name: 김파이, Balance: 15750.0

assert calc.add(10, 5) == 15
assert math_tool.gcd() == 6 and math_tool.lcm() == 36
assert str(my_account) == "Account: 123456789, Name: 김파이, Balance: 15750.0"
