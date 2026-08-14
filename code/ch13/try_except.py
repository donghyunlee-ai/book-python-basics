# code/ch13/try_except.py
# 02절 "죽지 않는 프로그램 — try와 except"의 예제 5~6개를 한 파일로 묶었다.
# 본문의 input() 대기 예제는 fact-checker가 자동 실행할 수 있도록
# unittest.mock.patch로 표준입력을 하드코딩했다(안전판). 본문 그대로의 형태는
# 각 함수 위 주석으로 보존한다.
from unittest.mock import patch


def crash_demo():
    """9장 1절 상황의 재현 — try/except 없이 그대로 두면 "삼" 입력에 죽는다.
    본문 원형:
        age_text = input("나이를 입력하세요: ")
        age = int(age_text)  # 여기서 "삼"이 들어오면 프로그램이 죽습니다.
        print(f"내년에는 {age + 1}살이 되시겠네요!")
    여기서는 죽는 상황을 실제로 재현하지 않고, 원인이 되는 변환만 보여준다.
    """
    age_text = "삼"
    try:
        age = int(age_text)
    except ValueError:
        print(f"(crash_demo) '{age_text}'는 정수로 바꿀 수 없어 ValueError가 납니다.")


def basic_try_except():
    # 에러가 날 수 있는 곳을 try로 감싸고, 실패할 때의 길을 except로 지정합니다.
    with patch("builtins.input", side_effect=["삼"]):
        try:
            age_text = input("나이를 입력하세요: ")
            age = int(age_text)
            print(f"내년에는 {age + 1}살이 되시겠네요!")
        except ValueError:
            print("숫자로만 입력해 주세요.")


def nameerror_not_caught():
    # 의도적으로 오타를 내어 만든 NameError가 except ValueError를 비껴가는지 확인합니다.
    with patch("builtins.input", side_effect=["20"]):
        try:
            age_text = input("나이를 입력하세요: ")
            age = int(age_text)
            # 일부러 오타를 냈습니다. age 대신 ag를 썼습니다.
            print(f"내년에는 {ag + 1}살이 되시겠네요!")  # noqa: F821 (의도된 오타)
        except ValueError:
            print("숫자로만 입력해 주세요.")


def read_loop_demo():
    # 제대로 된 숫자가 들어올 때까지 무한히 다시 묻는 실전 패턴입니다.
    # 안전판: 실제 무한 대기 대신 "삼" -> "7" 순서로 입력을 하드코딩합니다.
    with patch("builtins.input", side_effect=["삼", "7"]):
        while True:
            try:
                age_text = input("나이를 입력하세요: ")
                age = int(age_text)
                break  # 변환을 무사히 통과해 여기까지 오면 무한 루프를 탈출합니다.
            except ValueError:
                print("숫자로만 입력해 주세요. 다시 시도합니다.")

    print(f"입력하신 나이는 {age}살입니다.")


def read_int(prompt):
    # 수학 도우미의 입력 관문으로 사용할 수 있도록 함수로 부품화합니다.
    while True:
        try:
            user_input = input(prompt)
            return int(user_input)  # 변환 성공 시 값을 돌려주고 함수도 즉시 빠져나갑니다.
        except ValueError:
            print("숫자로만 입력해 주세요. 다시 시도합니다.")


def read_int_demo():
    with patch("builtins.input", side_effect=["삼", "20"]):
        age = read_int("나이를 입력하세요: ")
    print(f"내년에는 {age + 1}살이 되시겠네요!")


if __name__ == "__main__":
    crash_demo()
    basic_try_except()
    try:
        nameerror_not_caught()
    except NameError as e:
        print(f"(nameerror_not_caught) 예상대로 잡히지 않고 새어 나온 에러: {e}")
    read_loop_demo()
    read_int_demo()
