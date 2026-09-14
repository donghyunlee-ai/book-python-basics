# code/ch13/project/main.py
# 05절 "수학 도우미, 견고해지다" — 갑옷 세 겹을 입힌 견고화 main.py.
# ch12 main.py(구조) 위에 read_int·load_cache/save_cache·gcd raise 수신을 증분했다.
import os
from unittest.mock import patch

from mathtools.gcdlcm import gcd
from mathtools.prime import PrimeFinder


# --- 갑옷 ① 입력 관문 ---
def read_int(prompt):
    while True:
        try:
            text = input(prompt)
            # 아무것도 입력하지 않으면 "100"을 기본값으로 씁니다.
            text = text or "100"
            return int(text)
        except ValueError:
            print("숫자로 다시 입력해 주세요.")


def read_int_demo():
    # 안전판: 실제 터미널 대기 대신 "삼" -> "" (기본값) 순서를 하드코딩합니다.
    with patch("builtins.input", side_effect=["삼", ""]):
        n = read_int("몇까지 찾을까요? (기본 100): ")
    print(f"read_int 데모: 입력받은 값 = {n}")
    assert n == 100


# --- 갑옷 ② 캐시의 부활 ---
def load_cache(filename="primes.txt"):
    finder = PrimeFinder()
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                finder.primes.append(int(line.strip()))
        if finder.primes:
            finder.checked = finder.primes[-1]
        print(f"캐시 복원 완료: 소수 {len(finder.primes)}개")
    except FileNotFoundError:
        # 파일이 없으면 조용히 넘어갑니다(빈 캐시로 새 출발).
        print("저장된 캐시가 없습니다. 새로 시작합니다.")
    return finder


def save_cache(finder, filename="primes.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for p in finder.primes:
            f.write(f"{p}\n")
    print("캐시 저장 완료.")


# --- 갑옷 ③ 부품의 자기 방어(gcd raise)는 mathtools/gcdlcm.py에 있다 ---


if __name__ == "__main__":
    # primes.txt가 우연히 남아 있으면 "첫 실행" 시연이 어긋나므로 정리한다(안전판).
    if os.path.exists("primes.txt"):
        os.remove("primes.txt")

    read_int_demo()

    # 캐시가 없는 상태에서 복원을 시도하고, 소수를 찾은 뒤 저장합니다.
    finder = load_cache()
    print("이번 실행에서 새로 찾은 소수:", len(finder.find_up_to(200)))
    assert finder.count() == 46
    save_cache(finder)

    # 두 번째 실행 경로 재현: 캐시가 있는 상태의 출력(본문 둘째 블록)을 그대로 보여준다.
    # 복원 검증(안전판): 진도표까지 복원되므로 재탐색해도 중복 적재가 없다.
    finder2 = load_cache()
    assert finder2.checked == finder2.primes[-1] == 199
    newly_found = finder2.find_up_to(200)
    print("이번 실행에서 새로 찾은 소수:", len(newly_found))
    assert newly_found == [] and finder2.count() == 46
    save_cache(finder2)

    # 완성된 수학 도우미의 여러 실행을 보여줍니다.
    print(f"최대공약수 정상 계산: {gcd(12, 18)}")
    assert gcd(12, 18) == 6
    print(f"누적 소수 개수: {finder.count()}")

    try:
        result = gcd(12, 0)
        print(f"최대공약수: {result}")
    except ValueError as e:
        print(f"계산 실패: {e}")

    os.remove("primes.txt")  # 시연용 캐시 파일 정리(안전판)
