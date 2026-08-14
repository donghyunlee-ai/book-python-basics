# 9장 7절 [AI와 짝 코딩] 파일 처리 요청 — 인코딩·경로·닫기 누락을 의심하라 (오답 코드)
# 출력: FileNotFoundError (윈도우 절대경로가 코랩 환경에 없으므로 즉시 거절)

try:
    f = open("C:\\Users\\Default\\scores.txt", "r")
    data = f.read()
    print(data)
    raise AssertionError("예상과 다름: 에러가 나야 하는데 실행이 계속됨")
except FileNotFoundError as e:
    last_line = f"FileNotFoundError: {e!s}"
    print(last_line)
# 출력: FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Default\\scores.txt'
