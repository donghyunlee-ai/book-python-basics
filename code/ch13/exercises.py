# code/ch13/exercises.py
# 07절 연습문제 4개(예측형 1 + 구현형 1 + 리뷰형 2)의 실행 가능한 원본.
# input() 대기 예제는 unittest.mock.patch로 표준입력을 하드코딩했다(안전판).
from unittest.mock import patch


# --- 문항 1: 예외의 흐름 추적하기 ---
def q1_flow(user_input):
    print("--- 시작 ---")
    try:
        number = int(user_input)
        print(f"입력한 숫자: {number}")
    except ValueError:
        print("에러: 숫자가 아닙니다.")
    finally:
        print("--- 종료 ---")


def q1_demo():
    print("[시나리오 1: '7' 입력]")
    q1_flow("7")
    print("[시나리오 2: '삼' 입력]")
    q1_flow("삼")


# --- 문항 2: 끈질기게 다시 묻기 (완성된 정답) ---
def square_number():
    while True:
        try:
            user_input = input("제곱할 숫자를 입력하세요: ")
            number = int(user_input)
            return number ** 2
        except ValueError:
            print("숫자로만 입력해 주세요. 다시 시도합니다.")


def q2_demo():
    # 안전판: "삼" -> "5" 순서로 입력을 하드코딩합니다.
    with patch("builtins.input", side_effect=["삼", "5"]):
        result = square_number()
    print(f"계산 결과: {result}")
    assert result == 25


# --- 문항 3: 이 코드, 어디가 이상할까 (bare except가 NameError를 삼키는 버그) ---
def q3_buggy_demo(max_attempts=3):
    # 본문 원형은 while True: ... except: 로 무한 반복이지만(오타가 고쳐지지
    # 않으므로 매번 같은 거짓 안내가 나온다), fact-checker 실행 안전판으로
    # 시도 횟수 상한을 둔다.
    attempts = 0
    inputs = iter(["100", "3", "50", "2", "80", "4"])  # (총점, 과목 수) 3회분
    outputs = []
    with patch("builtins.input", side_effect=lambda _: next(inputs)):
        while attempts < max_attempts:
            attempts += 1
            try:
                total = int(input("총점: "))
                count = int(input("과목 수: "))
                # 의도적 오타: count가 아니라 cnt를 나누려고 시도합니다.
                average = total / cnt  # noqa: F821 (의도된 오타)
                print(f"평균: {average}")
                break
            except:  # noqa: E722 (bare except — 문항이 진단하는 바로 그 문제)
                msg = "숫자를 입력하세요. 다시 시작합니다."
                print(msg)
                outputs.append(msg)
    # 멀쩡한 입력("100"/"3" 등 숫자)에도 매번 같은 거짓 안내가 반복됨을 확인한다.
    assert len(outputs) == max_attempts
    assert all(o == "숫자를 입력하세요. 다시 시작합니다." for o in outputs)


def q3_narrowed_demo():
    # 진단: except:를 except ValueError:로 좁히면 숨어 있던 NameError가 드러난다.
    with patch("builtins.input", side_effect=["100", "3"]):
        try:
            total = int(input("총점: "))
            count = int(input("과목 수: "))
            average = total / cnt  # noqa: F821 (의도된 오타 — 좁히기 전 그대로)
            print(f"평균: {average}")
        except ValueError:
            print("숫자를 입력하세요. 다시 시작합니다.")
        except NameError as e:
            print(f"(q3_narrowed_demo) 좁히자 드러난 진범: {e}")
            assert str(e) == "name 'cnt' is not defined"


def q3_fixed_demo():
    # 오타(cnt -> count)까지 고친 최종 정답.
    with patch("builtins.input", side_effect=["100", "4"]):
        total = int(input("총점: "))
        count = int(input("과목 수: "))
        average = total / count
        print(f"평균: {average}")
    assert average == 25.0


# --- 문항 4: 이 코드, 어디가 이상할까 (방어 위치가 틀린 버그 -> 재배치 정답) ---
def q4_fixed_demo():
    # 해설의 정답 코드: int(user_input)을 try 안으로 옮기고 ValueError를 추가한다.
    inputs = iter(["삼", "0", "5"])
    with patch("builtins.input", side_effect=lambda _: next(inputs)):
        while True:
            user_input = input("100을 나눌 숫자를 입력하세요: ")
            try:
                number = int(user_input)
                result = 100 / number
                print(f"결과: {result}")
                break
            except ZeroDivisionError:
                print("0으로 나눌 수 없습니다. 다시 입력하세요.")
            except ValueError:
                print("숫자로만 입력해 주세요. 다시 입력하세요.")
    assert result == 20.0


if __name__ == "__main__":
    q1_demo()
    q2_demo()
    q3_buggy_demo()
    q3_narrowed_demo()
    q3_fixed_demo()
    q4_fixed_demo()
