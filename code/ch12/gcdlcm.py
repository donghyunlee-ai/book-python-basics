def gcd(a, b):
    answer = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            answer = i
    return answer

def lcm(a, b):
    return a * b // gcd(a, b)

# 직접 실행했을 때만 아래의 시험 코드가 돕니다.
if __name__ == "__main__":
    print("직접 실행했습니다. 시험 가동:", gcd(12, 18))
