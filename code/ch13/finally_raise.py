# code/ch13/finally_raise.py
# 04절 "뒷정리와 정직한 거절 — finally, else, raise"의 예제들을 묶었다.
import os


# --- finally: 무슨 일이 있어도 도는 칸 ---
def divide_and_cleanup(a, b):
    try:
        print(f"계산 시작: {a} / {b}")
        result = a / b
        print(f"결과: {result}")
    except ZeroDivisionError:
        print("에러: 0으로 나눌 수 없습니다.")
    finally:
        print("--- 작업 뒷정리 완료 ---\n")


def scenario_3_uncaught_demo():
    # 본문 원형(주석 처리된 상태로 둔다 — 3.12/3.14 전문 게재 예산 밖):
    # divide_and_cleanup(10, "2")
    # fact-checker 확인용: finally가 죽기 "직전"에 정말 찍히는지, 프로그램을
    # 통째로 죽이지 않고 바깥에서 안전하게 관찰한다(교육 코드 자체는 finally만
    # 쓰고 이 바깥 껍데기는 fact-checker 하네스일 뿐이다).
    try:
        divide_and_cleanup(10, "2")
    except TypeError as e:
        print(f"(scenario_3) finally 실행 후 새어 나온 에러 확인: {e}")


# --- with의 정체 회수: try/finally와 with의 등가 ---
def with_equivalence_demo():
    # 수동으로 뒷정리하기 (try/finally 방식)
    f = open("memo.txt", "w", encoding="utf-8")
    try:
        f.write("메모 남기기\n")
    finally:
        f.close()  # 중간에 에러가 나도 반드시 닫힌다.

    # 9장에서 배웠던 with 문법 (위와 완전히 같은 역할을 합니다)
    with open("memo.txt", "w", encoding="utf-8") as f:
        f.write("메모 남기기\n")

    os.remove("memo.txt")  # 시연용 파일 정리(안전판)


# --- else: 에러가 없었을 때만 도는 칸 ---
def else_demo():
    user_input = "2026"

    try:
        year = int(user_input)
    except ValueError:
        print("숫자가 아닙니다.")
    else:
        # 에러 없이 정수 변환에 성공했을 때만 실행됩니다.
        next_year = year + 1
        print(f"내년은 {next_year}년입니다.")


# --- raise: 이번엔 우리가 던진다 ---
class BankAccount:
    # 3인자, ch11 최종 정본을 그대로 재현한다
    # (fact-checker 실행용 최소 래퍼 — 본문은 deposit 메서드만 발췌한다).
    def __init__(self, account_num, name, balance):
        self.account_num = account_num  # 계좌번호 속성을 추가합니다
        self.name = name
        self.balance = balance

    # 11장 BankAccount 클래스의 입금 메서드 중 일부를 발췌했습니다.
    def deposit(self, amount):
        if amount <= 0:
            # 단순한 화면 출력이 아니라, 정식으로 에러를 쏘아 올려 거절합니다.
            raise ValueError("입금액은 0보다 커야 합니다.")

        self.balance += amount
        print(f"{amount}원 입금 완료. 잔액: {self.balance}원")


def raise_demo():
    # 부품이 던진 에러를, 이제는 사용하는 쪽에서 try/except로 잡아냅니다.
    account = BankAccount("123456789", "김파이", 10000)

    try:
        account.deposit(-5000)
    except ValueError as e:
        print(f"입금 실패: {e}")


if __name__ == "__main__":
    print("[시나리오 1: 무사히 통과할 때]")
    divide_and_cleanup(10, 2)

    print("[시나리오 2: except가 에러를 잡았을 때]")
    divide_and_cleanup(10, 0)

    print("[시나리오 3: 미처 못 잡은 에러로 죽을 때]")
    scenario_3_uncaught_demo()

    with_equivalence_demo()
    else_demo()
    raise_demo()
