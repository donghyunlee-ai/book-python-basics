# code/ch13/error_family.py
# 03절 "무엇을 잡을 것인가"의 예제 3개(다중 except, as e, bare except 삼킴)를 묶었다.
import os


def multi_except_demo(filename="numbers.txt"):
    # 에러의 종류에 따라 각기 다른 대피로를 만들어 안내문을 출력합니다.
    # numbers.txt가 없는 상태로 실행하면 FileNotFoundError 대피로를 탄다(의도된 시연).
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = f.read()
        number = int(data)
        result = 100 / number
        print(f"계산 결과: {result}입니다.")
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다. 파일 이름과 경로를 확인해 주세요.")
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다. 파일 안의 숫자를 확인해 주세요.")


def as_e_demo():
    # 에러가 품은 구체적인 설명을 e라는 이름표로 받아서 꺼내 봅니다.
    try:
        number = int("삼")  # noqa: F841 (본문 그대로: 실패를 보여주는 것이 목적)
    except ValueError as e:
        print("입력값이 올바르지 않습니다.")
        print(f"파이썬의 진짜 에러 메시지: {e}")


def bare_except_swallow_demo():
    # 개발자의 오타 때문에 터진 에러를 except:가 조용히 삼키고 거짓말을 합니다.
    try:
        # 사용자에게 올바른 숫자를 입력받았다고 가정해 보겠습니다.
        user_input = "50"
        number = int(user_input)

        # 개발자가 변수 이름에 오타를 냈습니다! (number -> namber)
        # 원래라면 여기서 NameError가 터지며 프로그램이 멈춰야 합니다.
        result = 100 / namber  # noqa: F821 (의도된 오타)
        print(f"결과는 {result}입니다.")
    except:  # noqa: E722 (bare except — 본문이 경계하는 바로 그 안티패턴)
        # 모든 에러를 조용히 삼켜 버리는 처리
        print("잘못된 입력입니다. 숫자를 확인해 주세요.")


if __name__ == "__main__":
    # numbers.txt가 우연히 남아 있으면 FileNotFoundError 경로 시연이 어긋나므로 정리한다.
    if os.path.exists("numbers.txt"):
        os.remove("numbers.txt")
    multi_except_demo()
    as_e_demo()
    bare_except_swallow_demo()
