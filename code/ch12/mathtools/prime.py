def is_prime_fast(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

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
