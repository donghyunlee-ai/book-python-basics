# code/ch13/chain_demo/chain_demo.py
# 01절 해부 2 — 호출 사슬 트레이스백 전문 게재 ②의 원본.
# simple_math.divide() 안에서 ZeroDivisionError가 터지는 2단 사슬을 재현한다.
# 실행: 이 디렉터리에서 `python3 chain_demo.py` (의도된 동작 — 크래시로 끝난다)
import simple_math

score = 100
people = 0
average = simple_math.divide(score, people)
