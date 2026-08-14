# 8장 3절 재료 건네기 — 위치·키워드 인자와 기본값

# [셀 1] 위치 인자 — 순서가 자리를 정한다
def power(base, exp):
    return base ** exp

print(power(2, 10))
print(power(10, 2))
# 출력: 1024 / 100

# [셀 2] 키워드 인자 — 이름으로 건넨다. 순서를 뒤집어도 결과는 동일
print(power(exp=10, base=2))
# 출력: 1024

# [셀 3] 3장에서 다루지 않고 미뤄 두었던 정렬 — sort(reverse=True)
scores = [85, 90, 70, 95, 80]
scores.sort(reverse=True)
print(scores)
# 출력: [95, 90, 85, 80, 70]

# [셀 4] 기본값 — 안 넣으면 대신 쓰인다
def greet(name, greeting="안녕"):
    print(f"{greeting}, {name}!")

greet("김파이")
greet("김파이", "반가워")
# 출력:
# 안녕, 김파이!
# 반가워, 김파이!

# [셀 5] 기본값이 있는 매개변수는 반드시 기본값이 없는 매개변수보다 뒤에 와야 한다
# 책의 코드(그대로 실행하면 에러로 멈추므로 여기서는 문자열로 확인합니다):
# def f(a=1, b):
#     pass
# 책에 실린 에러 메시지(파이썬 3.11 이하): SyntaxError: non-default argument follows default argument
# 파이썬 3.12 이상에서는 문구가 다르다: SyntaxError: parameter without a default follows parameter with a default
try:
    exec("def f(a=1, b):\n    pass\n")
    raise AssertionError("예상과 다름: 잘못된 배치인데 정의됨")
except SyntaxError as e:
    print("SyntaxError:", e)
    assert (
        "non-default argument follows default argument" in str(e)
        or "parameter without a default follows parameter with a default" in str(e)
    )

# [셀 6] 우리가 이미 써 온 것들 — print와 range 속의 위치·키워드·기본값
print("안녕", "파이썬", end="")
print(list(range(1, 10, 2)))
# 출력(줄바꿈 없는 end="" 탓에 한 줄로 이어짐): 안녕 파이썬[1, 3, 5, 7, 9]
