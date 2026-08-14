# 10장 4절 번호와 값을 한꺼번에 — enumerate

# [셀 1]
scores = [85, 90, 70, 95, 80]

# 7장 2절에서 배운 방법: 번호로 값을 찾아옵니다
for i in range(len(scores)):
    print(f"{i}번 학생의 점수: {scores[i]}")
# 출력:
# 0번 학생의 점수: 85
# 1번 학생의 점수: 90
# 2번 학생의 점수: 70
# 3번 학생의 점수: 95
# 4번 학생의 점수: 80

# [셀 2]
scores = [85, 90, 70, 95, 80]

# enumerate가 돌려주는 쌍의 실체 관찰
print(list(enumerate(scores)))
# 출력: [(0, 85), (1, 90), (2, 70), (3, 95), (4, 80)]

# [셀 3]
# 언패킹을 루프 변수에 적용한 직진 도구 enumerate
for i, score in enumerate(scores):
    print(f"{i}번 학생의 점수: {score}")
# 출력:
# 0번 학생의 점수: 85
# 1번 학생의 점수: 90
# 2번 학생의 점수: 70
# 3번 학생의 점수: 95
# 4번 학생의 점수: 80

# [셀 4]
# 합성수 목록
non_primes = [4, 6, 8, 9, 10]

# 두 번째 인자로 시작 번호를 1로 지정 (사람의 셈 기준)
for i, num in enumerate(non_primes, 1):
    print(f"[{i}] {num}")
# 출력:
# [1] 4
# [2] 6
# [3] 8
# [4] 9
# [5] 10

# [셀 5]
scores = [85, 90, 70, 95, 80]

# 시험 문제 오류로 모든 점수를 제자리에서 5점씩 올려 주어야 할 때
for i in range(len(scores)):
    scores[i] = scores[i] + 5

print("수정된 점수:", scores)
# 출력: 수정된 점수: [90, 95, 75, 100, 85]
