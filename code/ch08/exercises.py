# 8장 8절 연습문제

# [문항 1] 완전수 판별기 — perfect(n)
def perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

print(perfect(6))
print(perfect(28))
print(perfect(10))
assert perfect(6) is True
assert perfect(28) is True
assert perfect(10) is False
# 출력: True / True / False

# [문항 2] 각 자릿수의 합 구하기 — nsum(a)
def nsum(a):
    total = 0
    while a:
        total += a % 10
        a = a // 10
    return total

print(nsum(379))
print(nsum(19321))
assert nsum(379) == 19
assert nsum(19321) == 16
# 출력: 19 / 16

# [문항 3] 코드 리뷰형 — gcd의 경계 버그(min(a, b)까지 미포함)
def gcd_buggy(a, b):
    answer = 1
    for i in range(1, min(a, b)):
        if a % i == 0 and b % i == 0:
            answer = i
    return answer

print(gcd_buggy(12, 6))
assert gcd_buggy(12, 6) == 3  # 버그판: 6 자신이 검사 대상에서 빠져 3이 나온다

# 수정안: range(1, min(a, b) + 1)로 끝값을 하나 늘린다 (06절 정확판과 동일)
def gcd_fixed(a, b):
    answer = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            answer = i
    return answer

print(gcd_fixed(12, 6))
assert gcd_fixed(12, 6) == 6
# 출력: 3 (버그판) / 6 (수정판)

# [문항 4] 코드 리뷰형 — 반환 없는 함수가 낳는 None의 확산
def get_max(nums):
    biggest = nums[0]
    for n in nums:
        if n > biggest:
            biggest = n
    print("최댓값:", biggest)

biggest = get_max([3, 1, 4])
try:
    print(biggest * 2)
    raise AssertionError("예상과 다름: None과 곱셈했는데 성공함")
except TypeError as e:
    print("TypeError:", e)
    assert "unsupported operand type(s) for *: 'NoneType' and 'int'" in str(e)

# 수정안: print 대신 return biggest로 고치면 곱셈이 무사히 이루어진다
def get_max_fixed(nums):
    biggest = nums[0]
    for n in nums:
        if n > biggest:
            biggest = n
    return biggest

biggest_fixed = get_max_fixed([3, 1, 4])
print(biggest_fixed * 2)
assert biggest_fixed * 2 == 8
# 출력(버그판): 최댓값: 4 / TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
# 출력(수정판): 8
