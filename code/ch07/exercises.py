# 7장 8절 연습문제

# [셀 1]
i = 10
while i > 0:
    print(i)
    i -= 3

# [셀 2]
total = 0
for i in range(1, 100):
    total += i
print("1부터 100까지의 합:", total)

# [셀 3]
for num in range(2, 21):
    count = 0  
    
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
            
    if is_prime:
        count += 1

print(f"20 이하 소수의 개수: {count}")

# [셀 4]
total = 0
for i in range(3, 51, 3):
    total += i
print(total)

# [셀 5]
total = 0
for i in range(1, 101):
    total += i
print("1부터 100까지의 합:", total)

# [셀 6]
count = 0
for num in range(2, 21):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
            
    if is_prime:
        count += 1

print(f"20 이하 소수의 개수: {count}")

