# 파일의 맨 위, 또는 코랩의 첫 번째 셀에 모아 둡니다
import copy
import math
import random

# 1. math 모듈 -- 점(.) 도식의 세 번째 확장
result = math.sqrt(16)
print(result)  # 4.0

# 2. random 모듈 -- 실행마다 다른 값이 출력됩니다
dice = random.randint(1, 6)
print(dice)

# 3. copy 모듈 -- 3장의 얕은 복사 함정을 deepcopy로 해결
original = [[1, 2], [3, 4]]
copied = copy.deepcopy(original)

# 원본의 속 그릇을 고쳐도 사본은 무사합니다
original[0].append(99)
print("원본:", original)
print("사본:", copied)
