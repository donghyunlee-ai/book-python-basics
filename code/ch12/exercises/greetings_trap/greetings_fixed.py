# 문항4의 해설 코드 -- 가드를 세워 import 시에는 조용하다.
def say_hello(name):
    return f"안녕하세요, {name}님!"

if __name__ == "__main__":
    print("--- 모듈 시험 시작 ---")
    print(say_hello("김파이"))
    print("--- 모듈 시험 종료 ---")
