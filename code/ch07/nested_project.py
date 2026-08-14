# 7장 6절 중첩 루프와 수학 도우미의 출발 — GCD·소수 (러닝 프로젝트 시작점)

# [셀 1]
print("구구단 일부 출력:")
for i in range(3, 6, 2):
    print(f"--- {i}단 ---")
    for j in range(1, 4):
        print(f"{i} * {j} = {i * j}")

# [셀 2]
print("각 단의 3곱까지만 출력하고 건너뛰기:")
for i in range(3, 10, 2):
    print(f"--- {i}단 ---")
    for j in range(1, 10):
        if j == 4:
            break  # 안쪽 루프만 벗어납니다.
        print(f"{i} * {j} = {i * j}")

# [셀 3]
a = 12
b = 6
print(f"{a}와 {b}의 공약수:")
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        print(i)

# [셀 4]
a = 12
b = 6
gcd = 1
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        gcd = i
        break  # 첫 공약수에서 멈춥니다.
print(f"{a}와 {b}의 최대공약수: {gcd}")

# [셀 5]
lcm = (a * b) // gcd
print(f"{a}와 {b}의 최소공배수: {lcm}")

# [셀 6]
n = 7
is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
            
if is_prime:
    print(f"{n}은(는) 소수입니다.")
else:
    print(f"{n}은(는) 소수가 아닙니다.")

# [셀 7]
target_count = 5
count = 0
answer = 0

print("2부터 100 사이의 소수를 차례로 찾습니다:")
for n in range(2, 101):
    is_prime = True
    
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
            
    if is_prime:
        print(n, end=" ")  # 발견한 소수를 나열합니다.
        count += 1
        if count == target_count:
            answer = n
            break

print(f"\n{target_count}번째 소수: {answer}")

