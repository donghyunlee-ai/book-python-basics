def gcd(a, b):
    answer = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            answer = i
    return answer

def lcm(a, b):
    return a * b // gcd(a, b)
