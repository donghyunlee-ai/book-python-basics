# 1. from ... import: 도구 하나만 콕 집어 가져오고 점 없이 부른다
from math import sqrt

result = sqrt(16)
print(result)  # 4.0

# 2. as: 도구함을 가져오되 짧은 별칭을 붙여 점으로 부른다
import datetime as dt

today = dt.date(2026, 7, 12)
print(today)  # 2026-07-12

# 3. * (별표): 이름 충돌 위험 시범 (책은 이 형태를 쓰지 말라고 경고한다)
pi = 3.14
from math import *
print(pi)  # 3.141592653589793 (내가 만든 pi가 조용히 덮어써짐)

# 4. 세 형태 나란히 대조
import math
print(math.sqrt(16))

from math import sqrt
print(sqrt(16))

import math as m
print(m.sqrt(16))
