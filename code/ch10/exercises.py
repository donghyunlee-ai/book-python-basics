# ch10-08 연습문제 (본문 게재 코드 원본 — writer 기계적 추출, 미실행)
# 검증 대상(fact-checker 실행 예정): python3
# 각 문항은 "문제 원형(주석)" + "해설의 정답 코드(실행·assert)"로 구성합니다.

# [문항 1] 모음만 걸러서 세기
# 문제 원형:
# s = "hello world"
# vowels = []
# for c in s:
#     if c in "aeiou":
#         vowels.append(c)
# print(vowels)
# print("모음 개수:", len(vowels))
#
# 해설의 정답: 컴프리헨션 한 줄로 접기
s = "hello world"
vowels = [c for c in s if c in "aeiou"]
print(vowels)
print("모음 개수:", len(vowels))
assert len(vowels) == 3
# 출력:
# ['e', 'o', 'o']
# 모음 개수: 3

# [문항 2] 두 수의 공약수와 최대공약수
# 문제 원형:
# a = 12
# b = 6
# common_divisors = []  # [1, 2, 3, 6]이 나오도록 컴프리헨션으로 고칩니다.
#
# 해설의 정답: and로 두 나머지를 동시에 거르고, min(a, b) + 1까지 순회
a = 12
b = 6
common_divisors = [i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0]
print("공약수:", common_divisors)
print("최대공약수:", max(common_divisors))
assert common_divisors == [1, 2, 3, 6]
assert max(common_divisors) == 6
# 출력:
# 공약수: [1, 2, 3, 6]
# 최대공약수: 6

# [문항 3] 이 코드, 정말 개선일까 — 이름 목록 거르기와 표시
members = ["김파이", "이코드", "박파이썬", "최씨", "정데이터"]

# 동료가 자랑하는 "개선된" 한 줄 코드 (동작은 맞지만 읽기 어려워 03절 기준으로 탈락)
result = [f"[{'관리자' if m.startswith('김') else '회원'}] {m.replace('파이', 'Py')}" for m in members if len(m) >= 3 and m != "이코드"]
print(result)
assert result == ['[관리자] 김Py', '[회원] 박Py썬', '[회원] 정데이터']

# 해설이 권하는 정직한 여러 줄의 for 루프로 다시 쓴 등가 버전
result_loop = []
for m in members:
    if len(m) >= 3 and m != "이코드":
        role = "관리자" if m.startswith("김") else "회원"
        result_loop.append(f"[{role}] {m.replace('파이', 'Py')}")
assert result_loop == result
# 출력: ['[관리자] 김Py', '[회원] 박Py썬', '[회원] 정데이터']

# [문항 4] 이 코드, 어디가 이상할까 — enumerate의 하나 어긋남
primes = [2, 3, 5, 7, 11]

# 문제 원형: 소수 목록에 1번부터 번호를 매기려 했지만 0번부터 찍히는 조용한 오류
buggy_output = []
for i, p in enumerate(primes):
    buggy_output.append(f"[{i}번 소수] {p}")
print(buggy_output[0])
assert buggy_output[0] == "[0번 소수] 2"

# 해설의 정답: enumerate(primes, 1)로 시작 번호를 1로 지정
fixed_output = []
for i, p in enumerate(primes, 1):
    fixed_output.append(f"[{i}번 소수] {p}")
print(fixed_output[0])
assert fixed_output[0] == "[1번 소수] 2"
# 출력:
# [0번 소수] 2
# [1번 소수] 2
