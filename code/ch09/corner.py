# ch09-07 [AI와 짝 코딩] 파일 처리 요청 — 인코딩·경로·닫기 누락을 의심하라 (본문 게재 오답 코드, 1셀)
# 검증 대상(fact-checker 실행 예정): python3
# 출력: FileNotFoundError (윈도우 절대경로가 코랩 환경에 없으므로 즉시 거절)

try:
    f = open("C:\\Users\\Default\\scores.txt", "r")
    data = f.read()
    print(data)
    raise AssertionError("죽어야 하는데 살았음")
except FileNotFoundError as e:
    last_line = f"FileNotFoundError: {e!s}"
    print(last_line)
# 출력: FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Default\\scores.txt'
