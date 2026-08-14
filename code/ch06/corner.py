# ch06-06 [AI와 짝 코딩] 조건 분기 요청 (본문 게재 오답 코드 원본, 1셀)
# 검증 대상(fact-checker 실행 예정): python3
# 출력: B / C  (90점인데 A가 아닌 B·C가 찍히는 세 갈래 함정 실물 — 경계값 오류·
#       독립 if 중복 실행·빠뜨린 경우가 한 코드에 겹쳐 있다)

score = 90

if score > 90:
    print("A")
if score > 80:
    print("B")
if score > 70:
    print("C")
if score < 60:
    print("F")
