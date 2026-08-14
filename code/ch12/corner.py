# AI가 지어낸 존재하지 않는 모듈을 import하면 어떻게 되는지 검증한다.
try:
    import csv_summary_analyzer

    result = csv_summary_analyzer.summarize("data.csv")
    print(result)
except ModuleNotFoundError as e:
    # 본문에는 마지막 줄만 인용한다: "ModuleNotFoundError: No module named 'csv_summary_analyzer'"
    assert str(e) == "No module named 'csv_summary_analyzer'"
    print(f"ModuleNotFoundError: {e}")
