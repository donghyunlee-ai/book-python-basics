def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("0으로 나눌 수 없습니다.")
        return None
    return a / b

if __name__ == "__main__":
    print("--- calculator 직접 실행 ---")
    print(add(10, 5))
    print(divide(10, 0))
