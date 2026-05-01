def get_number(message):
    while True:
        try:
            num = int(input(message))
            return num
        except ValueError:
            print("'숫자'를 입력하세요.")


def get_operator():
    while True:
        op = input("연산자를 선택하세요 (+, -, *, /): ")

        if op in ["+", "-", "*", "/"]:
            return op
        else:
            print("잘못된 연산자를 선택하셨습니다.")


def get_second_number(op):
    while True:
        b = get_number("두 번째 숫자를 다시 입력해주세요: ")

        if op == "/" and b == 0:
            print("0으로 나눌 수 없습니다. 다시 입력해주세요.")
        else:
            return b


def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return("0으로 나눌 수 없습니다.")
        return a / b


def print_result(result):
    print("결과값은 ", result," 입니다.")


def should_continue():
    while True:
        yn = input("다시 계산기를 사용하시겠습니까? (y/n): ").lower()
   
        if yn == "y":
            return True
        elif yn == "n":
            return False
        else:
            print("y 혹은 n으로 대답해주세요.")


def main():
    print(f'{"  CaritaStar Calculator  ":=^40}')
    
    while True:
        num1 = get_number("첫 번째 숫자를 입력해주세요: ")
        print(f"첫 번째 입력된 값은 '{num1}'입니다.")
    
        op = get_operator()

        num2 = get_second_number(op)
        print(f"두 번째 입력된 값은 '{num2}'입니다.")

        result = calculate(num1, num2, op)

        print_result(result)

        if not should_continue():
            print("계산기를 종료합니다.")
            break


main()