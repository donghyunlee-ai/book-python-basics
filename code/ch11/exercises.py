# ch11-08 연습문제 (본문 게재 코드 원본 — writer 기계적 추출, 미실행)
# 검증 대상(fact-checker 실행 예정): python3
# 각 문항은 "문제 원형(주석)" + "해설의 정답 코드(실행·assert)"로 구성합니다.

# ===== 문항 1 — 계좌의 잔액 추적하기 =====
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

a = BankAccount("김파이", 1000)
b = BankAccount("이코드", 500)

a.withdraw(1500)
b.deposit(500)
b.withdraw(1000)

print(f"{a.name} 잔액: {a.balance}")
print(f"{b.name} 잔액: {b.balance}")
# 출력: 김파이 잔액: 1000
# 출력: 이코드 잔액: 0

assert a.balance == 1000  # 잔액보다 큰 출금은 거절되어 불변
assert b.balance == 0  # 잔액과 정확히 같은 경계값 출금은 성공

# ===== 문항 2 — 가장 큰 소수 찾기 =====
def is_prime_fast(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class PrimeFinder:
    def __init__(self):
        self.primes = []
        self.checked = 1

    def find_up_to(self, limit):
        new_primes = []
        for n in range(self.checked + 1, limit + 1):
            if is_prime_fast(n):
                self.primes.append(n)
                new_primes.append(n)
        if limit > self.checked:
            self.checked = limit
        return new_primes

    # 문제 원형(미완성):
    #     def largest(self):
    #         # 이 부분을 채워 보세요
    #         pass
    #
    # 해설의 정답 코드:
    def largest(self):
        if not self.primes:
            return None
        return self.primes[-1]

finder = PrimeFinder()
print("시작 직후:", finder.largest())  # None이 나와야 합니다.
finder.find_up_to(20)
print("20까지 찾은 후:", finder.largest())  # 19가 나와야 합니다.
# 출력: 시작 직후: None
# 출력: 20까지 찾은 후: 19

assert finder.largest() == 19

# ===== 문항 3 — 이 코드, 어디가 이상할까 =====
# 문제 원형(self.total_accounts += 1로 인해 클래스 변수가 가려지는 오답):
class BrokenBankAccount:
    total_accounts = 0

    def __init__(self, name):
        self.name = name
        self.total_accounts += 1  # 함정: 클래스 변수가 아니라 인스턴스 변수가 새로 생긴다

_broken_a = BrokenBankAccount("김파이")
_broken_b = BrokenBankAccount("이코드")
_broken_c = BrokenBankAccount("박튜플")
print("전체 계좌 수(오답):", BrokenBankAccount.total_accounts)
# 출력: 전체 계좌 수(오답): 0

# 해설의 정답 코드(BankAccount.total_accounts += 1로 한 줄만 고침):
class BankAccountCounter:
    total_accounts = 0

    def __init__(self, name):
        self.name = name
        BankAccountCounter.total_accounts += 1

fixed_a = BankAccountCounter("김파이")
fixed_b = BankAccountCounter("이코드")
fixed_c = BankAccountCounter("박튜플")

print("전체 계좌 수:", BankAccountCounter.total_accounts)
# 출력: 전체 계좌 수: 3

assert BrokenBankAccount.total_accounts == 0
assert BankAccountCounter.total_accounts == 3

# ===== 문항 4 — 이 설계, 클래스가 필요할까 =====
# 문제 원형(과잉 설계 — self를 쓰지 않는 StringTools 클래스):
class StringTools:
    def reverse(self, s):
        return s[::-1]

    def count_vowels(self, s):
        count = 0
        for char in s:
            if char in "aeiouAEIOU":
                count += 1
        return count

tools = StringTools()
print(tools.reverse("파이썬"))
print(tools.count_vowels("Hello"))
# 출력: 썬이파
# 출력: 2

# 해설의 정답 코드(불필요한 클래스 껍질을 벗겨낸 함수 두 개):
def reverse(s):
    return s[::-1]

def count_vowels(s):
    count = 0
    for char in s:
        if char in "aeiouAEIOU":
            count += 1
    return count

assert tools.reverse("파이썬") == reverse("파이썬") == "썬이파"
assert tools.count_vowels("Hello") == count_vowels("Hello") == 2
