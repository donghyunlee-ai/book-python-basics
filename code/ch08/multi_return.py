# ch08-04 여러 값 돌려주기 — 튜플 반환과 언패킹 (본문 게재 코드 원본 — writer 기계적 추출, 미실행)
# 검증 대상(fact-checker 실행 예정): python3

# [셀 1] return 뒤에 쉼표로 나열 — 파이썬이 하나의 튜플로 묶어 돌려준다
def min_max(nums):
    return min(nums), max(nums)

result = min_max([3, 1, 4])
print(result)
# 출력: (1, 4)

# [셀 2] 언패킹 — 튜플이 여러 이름표로 풀려 나뉜다
low, high = min_max([3, 1, 4])
print("최솟값:", low)
print("최댓값:", high)
# 출력:
# 최솟값: 1
# 최댓값: 4

# [셀 3] 단일 반환은 튜플로 포장되지 않는다 — 쉼표 유무가 반환값의 실체를 바꾼다
def square(x):
    # 괄호를 쳐서 돌려주더라도 쉼표가 없으면 튜플이 아닙니다.
    return (x * x)

print(type(square(5)))
print(type(min_max([3, 1, 4])))
# 출력:
# <class 'int'>
# <class 'tuple'>

# [셀 4] 언패킹 개수 불일치 — ValueError: not enough values to unpack (expected 3, got 2)
try:
    low, high, mid = min_max([3, 1, 4])
    raise AssertionError("도달하면 오류: 개수가 안 맞는데 언패킹 성공함")
except ValueError as e:
    print("ValueError:", e)
    assert "not enough values to unpack (expected 3, got 2)" in str(e)

# [셀 5] 개수를 확신할 수 없을 때는 통째로 받아 인덱스로 꺼낸다
result = min_max([3, 1, 4])
print("값의 차이:", result[1] - result[0])
# 출력: 값의 차이: 3
