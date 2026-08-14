# ch08-05 함수 안과 밖 — 지역·전역 변수 (본문 게재 코드 원본 — writer 기계적 추출, 미실행)
# 검증 대상(fact-checker 실행 예정): python3

# [셀 1] 지역 변수는 함수 밖에서 안 보인다 — NameError
def make_secret():
    secret = 1004
    print("함수 안:", secret)

make_secret()
try:
    print("함수 밖:", secret)
    raise AssertionError("도달하면 오류: 지역 변수가 밖에서도 보임")
except NameError as e:
    print("NameError:", e)
    assert "name 'secret' is not defined" in str(e)
# 출력(함수 안): 함수 안: 1004

# [셀 2] 간섭 없는 이름 공간 — 여러 함수가 같은 이름 total을 써도 서로 엉키지 않는다
def sum_scores(scores):
    total = 0
    for s in scores:
        total = total + s
    return total

def sum_prices(prices):
    total = 0
    for p in prices:
        total = total + p
    return total

print("점수 합:", sum_scores([80, 90, 100]))
print("가격 합:", sum_prices([1000, 2000]))
# 출력:
# 점수 합: 270
# 가격 합: 3000

# [셀 3] 밖의 변수(전역 변수)는 안에서 자유롭게 읽힌다
message = "전체 공지: 시스템 점검"

def show_notice():
    print("함수 안에서 읽음:", message)

show_notice()
# 출력: 함수 안에서 읽음: 전체 공지: 시스템 점검

# [셀 4] 할당의 함정 — 안에서 같은 이름에 값을 할당하면 새 지역 변수가 태어날 뿐
score = 50

def cheat():
    score = 100
    print("함수 안의 점수:", score)

cheat()
print("함수 밖의 원래 점수:", score)
# 출력:
# 함수 안의 점수: 100
# 함수 밖의 원래 점수: 50

# [셀 5] global — 밖의 변수를 명시적으로 고쳐 쓰는 뒷문 (지양할 것, 표지만 확인)
score = 50

def real_cheat():
    global score
    score = 100
    print("global로 강제 변경함:", score)

real_cheat()
print("함수 밖의 바뀐 점수:", score)
# 출력:
# global로 강제 변경함: 100
# 함수 밖의 바뀐 점수: 100

# [셀 6] 리스트를 넘기면 별칭(alias)이 함수 호출에서도 작용한다
def add_item(cart):
    cart.append("사과")
    print("함수 안에서 카트에 담았습니다:", cart)

my_cart = ["바나나"]
add_item(my_cart)
print("함수 밖의 내 카트:", my_cart)
# 출력:
# 함수 안에서 카트에 담았습니다: ['바나나', '사과']
# 함수 밖의 내 카트: ['바나나', '사과']
