# 5장 7절 [AI와 짝 코딩] 계산식 요청 — 나눗셈과 소수 비교를 의심하라
# 책의 오답 코드와, 좋은 요청이 기대하는 출력을 확인하는 코드

# --- 책의 오답 코드: AI가 제안한 장바구니 예산 확인 코드 (예시 데이터에선 통과) ---
prices = [10, 20]
budget = 30

total = sum(prices)
print(total == budget)  # True (예시 정수로는 통과)
assert (total == budget) is True

# --- 해설: 실전 소수 데이터를 넣으면 배신한다 ---
prices2 = [1.1, 2.2]
budget2 = 3.3
total2 = sum(prices2)
print(total2 == budget2)  # False (부동소수점 오차)
assert (total2 == budget2) is False

# --- 좋은 요청의 기대 출력 쌍 (round 비교로 정답) ---
assert round(sum([1.1, 2.2]), 2) == round(3.3, 2)          # 맞는 경우: True
assert round(sum([1.1, 1.1]), 2) != round(3.3, 2)          # 어긋나는 경우: False

print("corner.py: 모든 확인을 통과했습니다")
