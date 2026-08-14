# ch02-06 자료형 변환 — int, float, str 사이 건너기 (노트북 셀 기준 원본, 7셀 구성)
# 검증: python3 3.14.4 (스크립트) + IPython InteractiveShell 9.12.0 (셀 순차 실행, 2026-07-07 전 셀 확인)
# 에러 셀: 셀 5 ValueError — 새 세션에서 본문 순서(1~5)로 실행해 트레이스백 캡처, "Cell In[5]"가 본문 셀 순서와 일치
#          (typesetter: Colab 라이브 대조 목록 항목 — 마지막 줄
#           ValueError: invalid literal for int() with base 10: '삼' 은 불변)

# 셀 1 — 세 변환 함수 기본: 재료를 그 자료형으로 바꾼 "새 값"을 돌려준다 (str()은 05절 응급처치 회수)
print(int("12345"))   # 출력: 12345
print(float(3))       # 출력: 3.0
print(str(20))        # 출력: 20

# 셀 2 — 출력 생김새로는 변환 확인 불가(print는 따옴표를 안 보여줌) → type()으로 전후 검증 습관
print(type("12345"))        # 출력: <class 'str'>
print(type(int("12345")))   # 출력: <class 'int'>

# 셀 3 — 재할당 함정(오답 시연): int(a)는 새 값을 돌려줄 뿐, 받지 않으면 버려진다
#         a가 정수가 됐다면 a + "0"은 TypeError여야 하는데 — 에러 없이 "70"(글 잇기) = a는 여전히 str
a = "7"
int(a)            # 결과를 아무도 받지 않음 — 그 자리에서 버려짐
print(a + "0")    # 출력: 70  (칠십이 아니라 두 글자짜리 글)

# 셀 4 — 정답: 변환은 재할당해야 완성 (a = int(a))
a = "7"
a = int(a)
print(type(a))    # 출력: <class 'int'>
print(a + 3)      # 출력: 10

# 셀 5 — 모든 변환이 성립하지는 않는다: ValueError 실물 (본문 트레이스백 전문 게재)
# print(int("삼"))
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# Cell In[5], line 1
# ----> 1 print(int("삼"))
#
# ValueError: invalid literal for int() with base 10: '삼'

# 본문 인라인 언급 — int("3.5")도 ValueError (본문은 마지막 줄만 인용, python3/IPython 동일 문구 검증)
# print(int("3.5"))
# ValueError: invalid literal for int() with base 10: '3.5'

# 셀 6 — 같은 값이라도 float()에는 맞는 생김새
print(float("3.5"))   # 출력: 3.5

# 셀 7 — float→int는 잘라내기(반올림 아님): 4가 아니라 3
print(int(3.9))       # 출력: 3
