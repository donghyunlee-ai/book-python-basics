# 11장 6절 수학 도우미의 진화 — 소수를 기억하는 PrimeFinder

# [셀 1] 10장에서 완성한 속도 개선판 is_prime_fast — 판정은 함수, 기억은 클래스(분업)
def is_prime_fast(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# [셀 2] 기억을 품은 PrimeFinder — self.primes(누적 소수)와 self.checked(진도)
class PrimeFinder:
    def __init__(self):
        self.primes = []  # 찾은 소수들을 차곡차곡 쌓아 둘 기억
        self.checked = 1  # 여기까지는 확실히 조사했다는 진도 표시표

    def find_up_to(self, n):
        new_primes = []
        # 진도를 나간 바로 다음 숫자부터 목표 숫자까지만 훑습니다.
        for i in range(self.checked + 1, n + 1):
            if is_prime_fast(i):
                self.primes.append(i)
                new_primes.append(i)

        # 새로 훑은 범위가 기존 진도보다 앞서 나갔다면 진도표를 갱신합니다.
        if n > self.checked:
            self.checked = n

        # 이번 호출에서 "새로" 찾은 소수만 돌려줍니다.
        return new_primes

    def count(self):
        return len(self.primes)

# [셀 3] find_up_to(10) 손 추적용 — 작은 값으로 표와 대조
trace_finder = PrimeFinder()
trace_result = trace_finder.find_up_to(10)
print(trace_result)
print(trace_finder.primes)
print(trace_finder.checked)
# 출력: [2, 3, 5, 7]
# 출력: [2, 3, 5, 7]
# 출력: 10

# [셀 4] 캐시의 이득 — 첫 주문(100까지), 재호출(공짜), 이어서 200까지
f = PrimeFinder()

# 첫 주문: 1부터 100까지 찾아라
result100 = f.find_up_to(100)
print("100까지 처음 찾은 소수:", result100)
print(f"개수: {len(result100)}개")

# 똑같은 주문을 다시: 100까지 찾아라
result_again = f.find_up_to(100)
print("100까지 다시 찾은 결과:", result_again)

# 이어서 주문: 200까지 찾아라
result200 = f.find_up_to(200)
print("101~200 구간에서 새로 찾은 소수:", result200)
print(f"새로 찾은 개수: {len(result200)}개")
# 출력: 100까지 처음 찾은 소수: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# 출력: 개수: 25개
# 출력: 100까지 다시 찾은 결과: []
# 출력: 101~200 구간에서 새로 찾은 소수: [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
# 출력: 새로 찾은 개수: 21개

# [셀 5] 상태를 읽는 도구들 — count()·속성 직접 접근·음수 인덱스
print(f"누적 소수 개수: {f.count()}개")

# 속성에 직접 접근해 읽기
print(f"5번째 소수: {f.primes[4]}")  # 인덱스는 0부터 시작하므로 4
print(f"지금까지 찾은 가장 큰 소수: {f.primes[-1]}")
# 출력: 누적 소수 개수: 46개
# 출력: 5번째 소수: 11
# 출력: 지금까지 찾은 가장 큰 소수: 199

assert trace_result == [2, 3, 5, 7] and trace_finder.checked == 10
assert len(result100) == 25 and result_again == [] and len(result200) == 21
assert f.count() == 46
assert f.primes[4] == 11 and f.primes[-1] == 199
