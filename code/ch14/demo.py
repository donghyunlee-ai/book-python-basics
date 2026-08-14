# 14장 1절 종착지에서 보는 풍경 — 일곱 줄의 항해 기록
# 실행 위치: 이 파일과 titanic.csv를 같은 폴더(code/ch14/)에 두고 실행한다.
import pandas as pd

df = pd.read_csv("titanic.csv")
print(len(df))

print(df[["Name", "Sex", "Age", "Survived"]].head())

print(df["Survived"].mean())
print(df[df["Sex"] == "female"]["Survived"].mean())
print(df[df["Sex"] == "male"]["Survived"].mean())
