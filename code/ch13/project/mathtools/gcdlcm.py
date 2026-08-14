# 13장 5절 갑옷 ③ — gcd에 raise 관문을 추가한 견고판
# (12장 gcdlcm.py에 raise 관문을 더했다.)
def gcd(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("양의 정수만 받습니다.")

    answer = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            answer = i
    return answer


def lcm(a, b):
    return a * b // gcd(a, b)
