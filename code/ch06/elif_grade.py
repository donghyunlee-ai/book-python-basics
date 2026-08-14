# 6장 3절 여러 갈래 — elif와 성적 등급
# 출력: B 등급입니다. / A 등급입니다. / A 등급입니다.,B 등급입니다.,C 등급입니다.(반례)
#       / C 등급입니다.(순서 반례) / (출력 없음, else 누락 반례)

# 셀 1 — 성적 등급 elif 사슬. score=85일 때 첫 번째 참(>=80)에서 멈춥니다.
score = 85

if score >= 90:
    print("A 등급입니다.")
elif score >= 80:
    print("B 등급입니다.")
elif score >= 70:
    print("C 등급입니다.")
elif score >= 60:
    print("D 등급입니다.")
else:
    print("F 등급입니다.")

print("-" * 20)

# 셀 1b — score=95로 바꾸면 첫 번째 조건(>=90)에서 바로 멈춥니다(처음 하나만 실행).
score = 95

if score >= 90:
    print("A 등급입니다.")
elif score >= 80:
    print("B 등급입니다.")
elif score >= 70:
    print("C 등급입니다.")
elif score >= 60:
    print("D 등급입니다.")
else:
    print("F 등급입니다.")

print("-" * 20)

# 셀 2 — 반례: elif 대신 독립 if 3개로 쪼개면 95점이 A·B·C 모두에 걸립니다(중복 실행).
score = 95

if score >= 90:
    print("A 등급입니다.")
if score >= 80:
    print("B 등급입니다.")
if score >= 70:
    print("C 등급입니다.")

print("-" * 20)

# 셀 3 — 반례: 순서를 뒤집어 넓은 조건을 맨 위에 두면 95점도 C로 판정됩니다.
score = 95

if score >= 70:
    print("C 등급입니다.")
elif score >= 80:
    print("B 등급입니다.")
elif score >= 90:
    print("A 등급입니다.")
else:
    print("F 등급입니다.")

print("-" * 20)

# 셀 4 — 반례: else를 빠뜨리면 55점은 어떤 조건 그물에도 걸리지 않아 조용히 미끄러집니다.
score = 55

if score >= 90:
    print("A 등급입니다.")
elif score >= 80:
    print("B 등급입니다.")
elif score >= 70:
    print("C 등급입니다.")
elif score >= 60:
    print("D 등급입니다.")
# else 없음 — 55점은 출력 없이 조용히 통과됩니다.
