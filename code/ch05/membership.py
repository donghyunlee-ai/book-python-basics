# 5장 6절 들어 있는가 — in, not in, 그리고 연산자 지도

# 셀 1 — 불리언 결과를 변수에 담아 확인합니다. 없는지를 물을 때는 not in을 씁니다.
scores = [85, 90, 70, 95, 80]
result = 90 in scores

print(type(result))     # <class 'bool'>
print(result)            # True
print(100 not in scores)  # True

# 셀 2 — 문자열은 낱글자가 아니라 조각(부분 문자열) 단위로 확인합니다.
title = "파이썬 프로그래밍"
print("이썬" in title)  # True
print("프파" in title)  # False

# 셀 3 — 딕셔너리는 키만 확인합니다. 집합은 원소를 확인합니다.
phone = {"김파이": "010-1234-5678", "이코드": "010-1111-2222"}
print("김파이" in phone)             # True
print("010-1234-5678" in phone)      # False (in은 키만 본다)

winning_numbers = {4, 5, 6, 7, 8}
print(5 in winning_numbers)  # True
