# ch11-04 모두의 것, 각자의 것 — 클래스 변수와 __str__ (본문 게재 코드 원본 — writer 기계적 추출, 미실행)
# 검증 대상(fact-checker 실행 예정): python3

# [셀 1] 어느 실물의 것도 아닌 정보 — 클래스 변수
class BankAccountV1:
    # 클래스 변수: 설계도에 단 하나만 만들어져 공유됩니다
    total_accounts = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        # 생성될 때마다 은행 전체 계좌 수를 1씩 증가시킵니다
        BankAccountV1.total_accounts += 1

a1 = BankAccountV1("김파이", 5000.0)
b1 = BankAccountV1("이코드", 10000.0)

# 지금까지 만들어진 계좌는 모두 2개입니다
print(BankAccountV1.total_accounts)
# 출력: 2

# [셀 2] 두 층의 검색 — 실물 이름으로도 클래스 변수를 읽을 수 있다
# 파이썬은 실물에 변수가 없으면 설계도를 찾아 올라갑니다
print(a1.total_accounts)
print(b1.total_accounts)
# 출력: 2
# 출력: 2

# [셀 3] 조용한 가림 함정 — self로 클래스 변수에 할당하면 인스턴스 변수가 새로 생겨 가려버린다
class BrokenAccount:
    total_accounts = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        # 함정: 클래스 변수를 늘리려는 의도였지만...
        self.total_accounts += 1

c3 = BrokenAccount("박튜플", 3000.0)
d3 = BrokenAccount("최리스트", 4000.0)

# 은행 전체 계좌 수와 실물 c가 아는 계좌 수를 대조합니다
print(BrokenAccount.total_accounts)
print(c3.total_accounts)
# 출력: 0
# 출력: 1

# [셀 4] print(a)가 못생겼다 — __str__ 없는 실물은 주소를 찍는다
class BankAccountNoStr:
    def __init__(self, account_num, name, balance):
        self.account_num = account_num  # 계좌번호 속성을 추가합니다
        self.name = name
        self.balance = balance

a4 = BankAccountNoStr("123456789", "김파이", 5000.0)
print(a4)
# 출력 형태: <__main__.BankAccountNoStr object at 0x...> (주소는 실행마다 달라짐)

# [셀 5] __str__ 정의 — 실물이 스스로를 설명하는 문장을 정한다
class BankAccount:
    def __init__(self, account_num, name, balance):
        self.account_num = account_num
        self.name = name
        self.balance = balance

    # 실물이 화면에 출력될 때의 문장을 정합니다
    def __str__(self):
        return f"Account: {self.account_num}, Name: {self.name}, Balance: {self.balance:.1f}"

a5 = BankAccount("123456789", "김파이", 5000.0)
print(a5)
# 출력: Account: 123456789, Name: 김파이, Balance: 5000.0

# [셀 6] __str__은 print하지 않는다 — return 대신 print를 쓰면 TypeError
class WrongAccount:
    def __init__(self, account_num, name, balance):
        self.account_num = account_num
        self.name = name
        self.balance = balance

    def __str__(self):
        # 문자열을 돌려주지 않고 제자리에서 직접 출력해 버립니다
        print(f"Account: {self.account_num}, Name: {self.name}, Balance: {self.balance:.1f}")

bad = WrongAccount("123456789", "김파이", 5000.0)

# 본문 그대로의 형태(그대로 실행하면 이 파일 전체가 멈춥니다):
# print(bad)
# 출력: Account: 123456789, Name: 김파이, Balance: 5000.0
# 출력: TypeError: __str__ returned non-string (type NoneType)
#
# 검증용 안전판(TypeError가 실제로 발생하는지 확인):
try:
    print(bad)
except TypeError as e:
    print(f"TypeError: {e}")

assert BankAccountV1.total_accounts == 2
assert BrokenAccount.total_accounts == 0 and c3.total_accounts == 1
assert str(a5) == "Account: 123456789, Name: 김파이, Balance: 5000.0"
