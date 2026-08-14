# 8장 2절 돌려주기 — return과 None

# [셀 1] return이 값을 밖으로 내보낸다
def square(x):
    return x * x

result = square(5)
print("계산 결과:", result)
# 출력: 계산 결과: 25

# [셀 2] 반환값을 다른 계산식의 재료로 곧바로 섞어 쓴다
total = square(5) + square(3)
print("두 제곱의 합:", total)
# 출력: 두 제곱의 합: 34

# [셀 3] return과 print는 다른 일이다 — show는 화면에 찍기만 할 뿐 돌려주지 않는다
def show(x):
    print(x * x)

result = show(5)
print("result가 가리키는 값:", result)
# 출력:
# 25
# result가 가리키는 값: None

# [셀 4] square(반환)와 show(출력)를 겹쳐 실행 — None이 다음 print로 흘러드는 모습
print("square의 대답:", square(5))
print("show의 대답:", show(5))
# 출력:
# square의 대답: 25
# 25
# show의 대답: None

# [셀 5] return은 만나는 즉시 함수를 끝낸다 — 아래 문장은 실행되지 않는다
def test_return():
    print("이 문장은 실행됩니다.")
    return 100
    print("이 문장은 영원히 실행되지 않습니다.")

print(test_return())
# 출력:
# 이 문장은 실행됩니다.
# 100

# [셀 6] 조기 반환(early return) 패턴
def check_score(score):
    if score < 0 or score > 100:
        return "잘못된 점수입니다."

    # 올바른 점수일 때만 이 줄에 도착합니다
    return "정상 처리되었습니다."

print(check_score(150))
print(check_score(85))
# 출력:
# 잘못된 점수입니다.
# 정상 처리되었습니다.

# [셀 7] 함수의 계약 위반 — return을 빼먹으면 None이 조용히 퍼지다 뒤늦게 TypeError
def faulty_add(a, b):
    result = a + b
    # 실수로 return result를 빼먹음!

calc = faulty_add(10, 20)
try:
    print("계산 결과의 다음 작업:", calc + 5)
    raise AssertionError("예상과 다름: None과 덧셈했는데 성공함")
except TypeError as e:
    print("TypeError:", e)
    assert "unsupported operand type(s) for +: 'NoneType' and 'int'" in str(e)
