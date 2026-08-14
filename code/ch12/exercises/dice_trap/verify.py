# 문항 3 검증: dice_game.py는 표준 random 모듈을 import하려 하지만,
# 같은 폴더에 놓인 빈 random.py가 먼저 잡혀 AttributeError로 멈춘다.
# 본문 인용 자구(마지막 줄): "AttributeError: module 'random' has no attribute 'randint'"
# 3.14+에서는 파이썬이 파일명을 바꾸라는 안내를 덧붙인다(본문에서 "버전에 따라 안내 문구가
# 더 붙을 수 있다"고 명시). 이 스크립트는 현재 인터프리터로 dice_game.py를 실제 실행해
# 두 경우 모두를 허용하는 형태로 마지막 줄을 검증한다.
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).parent
BASE_MSG = "AttributeError: module 'random' has no attribute 'randint'"


def main():
    proc = subprocess.run(
        [sys.executable, "dice_game.py"],
        cwd=HERE,
        capture_output=True,
        text=True,
    )
    assert proc.returncode != 0, "빈 random.py 가림으로 실패해야 하는데 정상 종료됨"

    lines = [l for l in proc.stderr.splitlines() if l.strip()]
    last_line = lines[-1]

    assert last_line.startswith(BASE_MSG), (
        f"마지막 줄이 본문 인용 자구로 시작하지 않음: {last_line!r}"
    )
    # 3.12: 접미사 없음(본문 인용 그대로) / 3.14+: "(consider renaming ...)" 접미사 추가
    print(f"[{sys.version.split()[0]}] 마지막 줄: {last_line}")
    print("검증 통과: 본문 인용 자구와 일치")


if __name__ == "__main__":
    main()
