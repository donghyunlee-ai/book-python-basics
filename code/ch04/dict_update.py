# 4장 2절 딕셔너리 고쳐 쓰기 — 추가·수정, 그리고 없는 키
# 에러 셀(셀 4)은 try로 감싸 에러 마지막 줄만 출력한다.
#        노트북에서 새 세션으로 셀 1~4를 차례로 실행하면 트레이스백에 Cell In[4]가 보인다.
#        머리 형식은 환경마다 다를 수 있지만 마지막 줄 KeyError: '김코드'는 같다.
# 참고: phone은 1절에서 만든 딕셔너리(김파이·이코드 2쌍)다 — 셀 1이 다시 만든다.

# 셀 1 — 1절의 phone 재생성 (새 세션 대비): 쌍 두 개
phone = {"김파이": "010-1234-5678", "이코드": "010-9876-5432"}
print(len(phone))    # 출력: 2

# 셀 2 — 없는 키에 할당 = 추가: 그릇이 스스로 자란다 (2 → 3)
phone["박튜플"] = "010-5555-0000"
print(phone)    # 출력: {'김파이': '010-1234-5678', '이코드': '010-9876-5432', '박튜플': '010-5555-0000'}
print(len(phone))    # 출력: 3

# 셀 3 — 있는 키에 할당 = 수정: 같은 문법, len 불변 (3 그대로)
phone["이코드"] = "010-1111-2222"
print(phone)    # 출력: {'김파이': '010-1234-5678', '이코드': '010-1111-2222', '박튜플': '010-5555-0000'}
print(len(phone))    # 출력: 3

# 셀 4 — 없는 키 읽기 = KeyError
#        책에서는 try 없이 phone["김코드"]만 실행해 트레이스백 전체를 보여 준다 (01절에서 예측해 보라고 한 코드)
try:
    phone["김코드"]
except KeyError as e:
    print("KeyError:", repr(e.args[0]))    # 에러 마지막 줄: KeyError: '김코드'

# 셀 5 — 안전하게 묻기: get은 에러 대신 None, 기본값도 정할 수 있다
print(phone.get("김코드"))    # 출력: None
print(phone.get("김코드", "미등록"))    # 출력: 미등록

# 셀 6 — 삭제는 pop(키): 값을 돌려주면서 쌍이 빠진다 (3 → 2)
print(phone.pop("박튜플"))    # 출력: 010-5555-0000
print(phone)    # 출력: {'김파이': '010-1234-5678', '이코드': '010-1111-2222'}
print(len(phone))    # 출력: 2

# --- 더 알아보기: 책의 설명을 직접 확인하는 코드(책에는 없음) ---
# - 리스트는 없는 번호 칸에 대입 불가: [10, 20][5] = 1 → IndexError: list assignment index out of range
# - 없는 키 pop도 KeyError: phone.pop("김코드") → KeyError: '김코드'
try:
    lst = [10, 20]; lst[5] = 1
except IndexError as e:
    print("(더 알아보기) IndexError:", e)    # list assignment index out of range
try:
    phone.pop("김코드")
except KeyError as e:
    print("(더 알아보기) KeyError:", repr(e.args[0]))    # KeyError: '김코드'
