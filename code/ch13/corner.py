# code/ch13/corner.py
# 06절 [AI와 짝 코딩] — bare except가 오타(NameError)까지 삼키는 오답 코드 원본.
def process_data(data_string):
    try:
        value = int(data_string)
        result = 100 / valeu  # noqa: F821 (오타가 숨어 있습니다 — 의도된 버그)
        return result
    except:  # noqa: E722 (bare except — 이 코너가 경계하는 안티패턴 그 자체)
        print("오류가 발생했습니다")
        return None


if __name__ == "__main__":
    output = process_data("10")
    print(output)
    # 거짓 안내를 냈는지(입력은 멀쩡한데 오타 때문에 삼켜졌는지) 확인한다.
    assert output is None
