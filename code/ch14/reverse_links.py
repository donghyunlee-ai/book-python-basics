# ch14 02절: "새 문법은 없었다" — 데모 코드 조각의 재관찰(역연결).
# 실행 위치: 이 파일과 titanic.csv를 같은 폴더(code/ch14/)에 두고 실행한다.
# fact-checker 중점: 참/거짓 열 head() 출력 자구, type(df) 출력 자구.
import pandas as pd

df = pd.read_csv("titanic.csv")

# 4장의 딕셔너리처럼 열을 꺼내고, 3장의 메서드처럼 답만 받습니다.
print(df["Survived"].mean())

# 비교 연산의 결과가 값 하나가 아니라 '참/거짓의 열'로 나옴을 확인합니다.
print((df["Sex"] == "female").head())

# df라는 변수에 담긴 값의 진짜 정체를 확인합니다.
print(type(df))
