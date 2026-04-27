print("미니계산기 입니다. 계산해야할 정수 두 개를 차례대로 입력하세요.")

while True :
    try :
        a = int(input("첫 번째 정수를 입력하세요 : "))
        b = int(input("두 번째 정수를 입력하세요 : "))
    except ValueError :
        print("숫자를 입력해주세요.")
        continue
    op = input("연산을 선택하세요 (+, -, *, /) : ")

    if op == "+" :
        print(f"연산결과 : {a + b}")
    elif op == "-" :
        print(f"연산결과 : {a - b}")
    elif op == "*" :
        print(f"연산결과 : {a * b}")
    elif op == "/" :
        if b==0 :
            print("0으로 나눌 수 없습니다.")
        else :
            print(f"연산결과 : {a / b}")
    else :
        print("잘못된 연산입니다.")

    again = input("계속할까요? (y/n) : ")

    if again == "n" :
        break
