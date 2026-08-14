# ch08-01 부품으로 만들기 — 함수 정의와 호출 (본문 게재 코드 원본 — writer 기계적 추출, 미실행)
# 검증 대상(fact-checker 실행 예정): python3

# [셀 1] def만 하면 등록될 뿐 실행되지 않는다 — 이어서 호출해야 비로소 돈다
def greet():
    print("안녕하세요!")
    print("파이썬의 세계에 오신 것을 환영합니다.")

# [셀 2] 호출(call) — 여기서야 두 줄이 찍힌다
greet()
# 출력:
# 안녕하세요!
# 파이썬의 세계에 오신 것을 환영합니다.

# [셀 3] 매개변수(parameter) x — 재료를 받는 빈자리
def square(x):
    result = x * x
    print(f"입력한 숫자의 제곱은 {result}입니다.")

# [셀 4] 인자(argument) — 실제로 건네는 값. 매번 다른 값을 꽂아 재사용한다
square(5)
square(9)
# 출력:
# 입력한 숫자의 제곱은 25입니다.
# 입력한 숫자의 제곱은 81입니다.

# [셀 5] 부품으로 묶기 전: 복사된 코드
price1 = 10000
tax1 = price1 * 0.1
total1 = price1 + tax1
print(f"최종 금액: {total1}원")

price2 = 15000
tax2 = price2 * 0.1
total2 = price2 + tax2
print(f"최종 금액: {total2}원")

price3 = 30000
tax3 = price3 * 0.1
total3 = price3 + tax3
print(f"최종 금액: {total3}원")

# [셀 6] 부품으로 묶은 후: 함수 정의와 호출
def print_total_price(price):
    tax = price * 0.1
    total = price + tax
    print(f"최종 금액: {total}원")

print_total_price(10000)
print_total_price(15000)
print_total_price(30000)
# 출력(셀 5·6 공통): 최종 금액: 11000.0원 / 최종 금액: 16500.0원 / 최종 금액: 33000.0원

# [셀 7] 인자 개수 부족 — TypeError: square() missing 1 required positional argument: 'x'
try:
    square()
    raise AssertionError("도달하면 오류: 인자 부족인데 실행됨")
except TypeError as e:
    print("TypeError:", e)
    assert "missing 1 required positional argument: 'x'" in str(e)

# [셀 8] 인자 개수 초과 — TypeError: square() takes 1 positional argument but 2 were given
try:
    square(1, 2)
    raise AssertionError("도달하면 오류: 인자 초과인데 실행됨")
except TypeError as e:
    print("TypeError:", e)
    assert "takes 1 positional argument but 2 were given" in str(e)
