# 11장 1절 데이터와 동작을 하나로 — 객체라는 관점

# [셀 1] 변수 산개의 불편 — 계좌가 늘어날수록 이름·잔액 변수가 흩어진다
name1 = "김파이"
balance1 = 0

name2 = "이코드"
balance2 = 0

def deposit(current_balance, amount):
    return current_balance + amount

# 함수는 그저 값을 뱉을 뿐, 계좌에 속해 있지 않습니다
balance1 = deposit(balance1, 10000)
print(f"{name1}의 잔액: {balance1}원")
# 출력: 김파이의 잔액: 10000원

# [셀 2] 딕셔너리로 반걸음 — 데이터는 묶였지만 동작은 여전히 밖에 있고, 오타 키는 조용히 통과한다
account = {"name": "김파이", "balance": 0}

def deposit_dict(acc, amount):
    acc["balance"] += amount

deposit_dict(account, 10000)

# 치명적인 오타: 에러 없이 'balence'라는 새 키가 생겨버립니다
account["balence"] = 5000

print("원래 잔액:", account["balance"])
print("딕셔너리 안쪽:", account)
# 출력: 원래 잔액: 10000
# 출력: 딕셔너리 안쪽: {'name': '김파이', 'balance': 10000, 'balence': 5000}

# [셀 3] type()과 점 표기 다시 보기 — 우리는 이미 객체를 써 왔다
# 2장부터 늘 보던 이 결과의 'class'가 바로 그 클래스입니다.
print(type(3))
print(type("hello"))
# 출력: <class 'int'>
# 출력: <class 'str'>

# list라는 설계도로 만든 실물(scores)이, 자신에게 딸린 동작(append)을 수행합니다.
scores = [10, 20]
scores.append(30)
print(scores)
# 출력: [10, 20, 30]

assert account["balance"] == 10000
assert account["balence"] == 5000
assert scores == [10, 20, 30]
