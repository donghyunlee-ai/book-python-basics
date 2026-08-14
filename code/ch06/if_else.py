# ch06-02 아니면 — else로 두 갈래 (본문 게재 코드 원본, 5셀 구성)
# 검증 대상(fact-checker 실행 예정): python3
# 출력: 아쉽지만 다음 기회에 도전해 주세요. / 불합격입니다. / (셀 2 SyntaxError: expected ':')
#       / 우산을 챙깁니다. / 문을 나섭니다. / 7은(는) 홀수입니다. / 판정을 종료합니다.

# 셀 1 — 55점을 if-else 두 갈래로 판정합니다.
score = 55

if score >= 60:
    print("축하합니다.")
    print("합격입니다.")
else:
    print("아쉽지만 다음 기회에 도전해 주세요.")
    print("불합격입니다.")

print("-" * 20)

# 셀 2 — else에 조건을 덧붙이면 SyntaxError입니다 (실행하면 아래 셀들이 돌지 않으므로 주석 처리):
# score = 55
#
# if score >= 60:
#     print("합격입니다.")
# else score < 60:
#     print("불합격입니다.")
#
# SyntaxError: expected ':'

# 셀 3 — if와 else 중 반드시 하나만 실행됩니다.
is_raining = True

print("외출 준비를 합니다.")

if is_raining:
    print("우산을 챙깁니다.")
else:
    print("선글라스를 챙깁니다.")

print("문을 나섭니다.")

print("-" * 20)

# 셀 4 — 짝수·홀수 판정에 else의 '나머지 전부' 성질을 활용합니다.
number = 7

if number % 2 == 0:
    print(f"{number}은(는) 짝수입니다.")
else:
    print(f"{number}은(는) 홀수입니다.")

print("-" * 20)

# 셀 5 — else를 빠뜨리면 거짓일 때 조용히 아무것도 출력하지 않습니다(조용한 오류).
score = 45

if score >= 60:
    print("합격입니다.")

print("판정을 종료합니다.")
