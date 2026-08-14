# ch04-02 딕셔너리 고쳐 쓰기 — 추가·수정, 그리고 없는 키 (노트북 셀 기준 원본, 6셀 구성)
# 검증: python3 실행 (2026-07-11) — 에러 셀(셀 4)은 try로 감싸 마지막 줄 문구 대조.
#        트레이스백 전문은 IPython 9.12.0 InteractiveShell 새 세션 순차 실행
#        (store_history=True)으로 캡처 — 본문 셀 순서 = 실행 번호(Cell In[4]).
#        마지막 줄 KeyError: '김코드' 불변, 머리 형식은 typesetter Colab 라이브 대조 대상.
# 주의: phone은 ch04-01의 관통 예제(김파이·이코드 2쌍, 수치 변경 금지) — 셀 1이 재생성.
#        수정 대상은 이코드(김파이의 010-1234-5678은 ch04-03 values() 검사·08절 문항 4가
#        이어 쓰므로 건드리지 않는다). 절 끝 상태: 김파이 원래 번호 + 이코드 010-1111-2222 (2쌍).

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

# 셀 4 — 없는 키 읽기 = KeyError (본문은 트레이스백 전문 게재 — 장 유일)
#        본문 게재 형태: phone["김코드"]  (베어 실행 — 01절 예측 숙제 문면 그대로)
try:
    phone["김코드"]
except KeyError as e:
    print("KeyError:", repr(e.args[0]))    # 마지막 줄 대조: KeyError: '김코드'

# 셀 5 — 안전하게 묻기: get은 에러 대신 None, 기본값도 정할 수 있다
print(phone.get("김코드"))    # 출력: None
print(phone.get("김코드", "미등록"))    # 출력: 미등록

# 셀 6 — 삭제는 pop(키): 값을 돌려주면서 쌍이 빠진다 (3 → 2)
print(phone.pop("박튜플"))    # 출력: 010-5555-0000
print(phone)    # 출력: {'김파이': '010-1234-5678', '이코드': '010-1111-2222'}
print(len(phone))    # 출력: 2

# 본문 산문 근거 검증 (게재 코드 아님):
# - 리스트는 없는 번호 칸에 대입 불가: [10, 20][5] = 1 → IndexError: list assignment index out of range
# - 없는 키 pop도 KeyError: phone.pop("김코드") → KeyError: '김코드'
try:
    lst = [10, 20]; lst[5] = 1
except IndexError as e:
    print("검증:", e)    # list assignment index out of range
try:
    phone.pop("김코드")
except KeyError as e:
    print("검증: KeyError:", repr(e.args[0]))    # KeyError: '김코드'
