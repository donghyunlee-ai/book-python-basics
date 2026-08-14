# ch04-04 집합 — 중복을 거절하는 그릇
# 본문 셀 원본. python3 실행 검증용.
# 규율: 예제는 숫자 집합 위주(문자열 집합은 출력 순서 비보장 — 본문 확정 서술 금지)

# [셀 1] 중복 소거 관찰 + type
numbers = {1, 2, 2, 3}
print(numbers)
print(type(numbers))
# 출력: {1, 2, 3}
# 출력: <class 'set'>

# [셀 2] 빈 중괄호의 주인은 딕셔너리 — 빈 집합은 set()
print(type({}))
print(type(set()))
# 출력: <class 'dict'>
# 출력: <class 'set'>

# [셀 3] 순서가 없으므로 번호로 못 집는다 — 본문은 마지막 줄만 인용
try:
    print(numbers[0])
except TypeError as e:
    print(f"TypeError: {e}")
# 마지막 줄: TypeError: 'set' object is not subscriptable

# [셀 4] "집합=정렬 그릇" 오해 반박 — 넣은 순서도 크기순도 아닌 출력
# 주의: 이 출력은 파이썬 버전 의존(해시 충돌 프로빙) — 3.14 {20, 100, 5} / ≤3.13(Colab 3.12) {100, 20, 5}
# 따라서 본문은 출력 블록을 싣지 않고 비확정 산문 처리(버전 정책, memory.md 「버전 고정」 참조)
print({100, 5, 20})
# 참고 출력(Colab 3.12 기준): {100, 20, 5}

# [셀 5] add — 새 원소 추가
numbers.add(4)
print(numbers)
# 출력: {1, 2, 3, 4}

# [셀 6] 이미 있는 원소를 add하면? — 조용한 무시(len 불변)
numbers.add(2)
print(numbers)
print(len(numbers))
# 출력: {1, 2, 3, 4}
# 출력: 4

# [셀 7] remove — 없는 원소는 KeyError(본문은 마지막 줄만 인용)
numbers.remove(4)
print(numbers)
# 출력: {1, 2, 3}
try:
    numbers.remove(9)
except KeyError as e:
    print(f"KeyError: {e}")
# 마지막 줄: KeyError: 9

# [셀 8] in — 집합의 주특기
print(7 in {1, 3, 5, 7})
# 출력: True
