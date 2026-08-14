# 8장 7절 [AI와 짝 코딩] 함수 요청 — 명세가 곧 프롬프트, 반환 없는 함수를 의심하라
# (AI가 내놓기 쉬운 오답 코드)
# 출력: 84.0 / 평균: None / total의 정체: <class 'NoneType'>
#       (나쁜 요청이 낳은 반환 없는 average — result가 None이 된다)

def average(nums):
    # 결과를 반환하지 않고 화면에 찍기만 합니다.
    print(sum(nums) / len(nums))

scores = [85, 90, 70, 95, 80]
total = average(scores)

# total을 이어지는 계산에 쓰려 하면 어떻게 될까요?
print("평균:", total)
print("total의 정체:", type(total))
assert total is None

# --- 좋은 요청이 요구하는 계약: 반환값이 있고, 빈 리스트는 0을 반환 ---
def good_average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

assert good_average([85, 90, 70, 95, 80]) == 84.0
assert good_average([]) == 0
print(good_average([85, 90, 70, 95, 80]))
print(good_average([]))
