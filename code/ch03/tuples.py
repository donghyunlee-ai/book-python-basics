# ch03-06 튜플 — 바꿀 수 없어서 쓸모 있는
# 본문 셀 순서대로. python3 실행 검증용 원본.
# 트레이스백 캡처(셀 3)는 IPython(anaconda 3.12.13) 새 세션 순차 실행 — capture_traceback.py 참조.

# --- 셀 1: 소괄호가 튜플을 만든다 ---
point = (3, 7)
print(point)         # (3, 7)
print(type(point))   # <class 'tuple'>

# --- 셀 2: 규칙 확인 — 인덱스·슬라이스·len·in 전부 그대로 ---
birth = (2007, 3, 14)
print(birth[0])      # 2007
print(birth[-1])     # 14
print(birth[0:2])    # (2007, 3)
print(len(birth))    # 3
print(2007 in birth) # True

# --- 셀 3: 칸 고쳐 쓰기 거절 — TypeError (본문 트레이스백 전문, 장 유일) ---
try:
    point[0] = 5
except TypeError as e:
    print(f"TypeError: {e}")   # TypeError: 'tuple' object does not support item assignment

# --- 셀 4: append 거절 — AttributeError (마지막 줄 인용만) ---
try:
    point.append(9)
except AttributeError as e:
    print(f"AttributeError: {e}")   # AttributeError: 'tuple' object has no attribute 'append'

# --- 셀 5: 문자열도 같은 거절 — TypeError (마지막 줄 인용만, ch03-05 약속 회수) ---
s = "hello"
try:
    s[0] = "H"
except TypeError as e:
    print(f"TypeError: {e}")   # TypeError: 'str' object does not support item assignment

# --- 셀 6: 언패킹 — 다중 할당과 맞바꾸기 ---
x, y = 10, 20
print(x)   # 10
print(y)   # 20
x, y = y, x
print(x)   # 20
print(y)   # 10

# --- 셀 7: 변환 왕복 — list()로 건너가 고치고 tuple()로 복귀 (재할당해야 완성) ---
t = (1, 2, 3)
temp = list(t)
temp.append(4)
t = tuple(temp)
print(t)                 # (1, 2, 3, 4)
print(list("파이썬"))    # ['파', '이', '썬']

# --- 본문 산문 주장 검증(게재 안 함) ---
# 괄호 없이 쉼표만으로도 튜플이다
pair = 3, 7
assert pair == (3, 7) and type(pair) is tuple
# 튜플 슬라이스의 결과도 튜플이다 (본문 "잘라낸 조각도 튜플" 서술)
assert birth[0:2] == (2007, 3) and type(birth[0:2]) is tuple
# 언패킹의 오른쪽은 튜플: 개수가 어긋나면 거절 (본문 서술 없음 — 범위 밖, 참고 확인만)
# 튜플 별칭은 무엇을 해도 탈이 없다 (본문 "별칭 안전" 서술의 실검증)
u = (1, 2, 3)
v = u
u = u + (4,)   # 재할당(이름표 옮기기)일 뿐 — v는 옛 튜플 그대로
assert v == (1, 2, 3)
