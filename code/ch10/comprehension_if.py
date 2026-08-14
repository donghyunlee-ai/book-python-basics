# ch10-03 거르기와 고르기 — 조건이 붙은 컴프리헨션 (본문 게재 코드 원본 — writer 기계적 추출, 미실행)
# 검증 대상(fact-checker 실행 예정): python3

# [셀 1]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens_comp = [n for n in nums if n % 2 == 0]
print(evens_comp)
# 출력: [2, 4, 6, 8, 10]

# [셀 2]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens_loop = []
for n in nums:
    if n % 2 == 0:
        evens_loop.append(n)
print(evens_loop)
# 출력: [2, 4, 6, 8, 10]

# [셀 3]
n = 3
parity = "짝" if n % 2 == 0 else "홀"
print(parity)
# 출력: 홀

# [셀 4]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
labels = ["짝" if n % 2 == 0 else "홀" for n in nums]
print(labels)
# 출력: ['홀', '짝', '홀', '짝', '홀', '짝', '홀', '짝', '홀', '짝']

# [셀 5]
# 본문 그대로의 형태(문법 자체가 틀린 코드 — 그대로 실행하면 이 파일 전체가 멈춥니다):
# nums = [1, 2, 3]
# bad_comp = [n for n in nums if n % 2 == 0 else 0]
# 출력: SyntaxError: invalid syntax
#
# 검증용 안전판(SyntaxError가 실제로 발생하는지 exec로 격리 확인):
try:
    exec("nums = [1, 2, 3]\nbad_comp = [n for n in nums if n % 2 == 0 else 0]")
except SyntaxError as e:
    print(f"SyntaxError: {e}")

# [셀 6]
users = [{"나이": 15}, {"나이": 22}, {"나이": 25}, {"나이": 31}, {"나이": 35}]

# 나쁜 예: 읽기를 포기하게 만드는 겹친 한 줄
status = ["통과" if u["나이"] >= 20 else "거절" for u in users if u["나이"] % 5 == 0]

# 좋은 예: 목적과 흐름이 확실히 보이는 루프
status_loop = []
for u in users:
    if u["나이"] % 5 == 0:
        if u["나이"] >= 20:
            status_loop.append("통과")
        else:
            status_loop.append("거절")

print(status == status_loop)
print(status_loop)
assert status == status_loop
# 출력:
# True
# ['거절', '통과', '통과']

# [셀 7]
# 2단부터 9단까지의 결과를 담은 2차원 리스트
gugu = [[i * j for j in range(1, 10)] for i in range(2, 10)]

# 2단(첫 항목)과 9단(마지막 항목) 확인
print(gugu[0])
print(gugu[-1])
# 출력:
# [2, 4, 6, 8, 10, 12, 14, 16, 18]
# [9, 18, 27, 36, 45, 54, 63, 72, 81]
