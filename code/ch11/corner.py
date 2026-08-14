# 11장 7절 [AI와 짝 코딩] 클래스 설계 요청 — 과잉 설계를 의심하라

# [셀 1] 나쁜 요청("클래스로 체계적으로 짜 줘")의 결과 — self를 한 번도 쓰지 않는 오답 실물
class TemperatureConverter:
    def __init__(self):
        # 기억할 상태가 없는데도 자리만 차지합니다.
        pass

    def c_to_f(self, celsius):
        # 섭씨를 화씨로 변환합니다. self를 쓰지 않습니다.
        return celsius * 9 / 5 + 32

    def f_to_c(self, fahrenheit):
        # 화씨를 섭씨로 변환합니다. self를 쓰지 않습니다.
        return (fahrenheit - 32) * 5 / 9

converter = TemperatureConverter()
print(f"섭씨 20도는 화씨 {converter.c_to_f(20)}도입니다.")
# 출력: 섭씨 20도는 화씨 68.0도입니다.

assert converter.c_to_f(20) == 68.0
assert converter.f_to_c(68.0) == 20.0
