def plus(a, b):
    return a+b
def minus(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b

i = 1
while i != 0:
    calculate = input("'+ - * / 종료' 중 하나를 입력하세요")
    if calculate == "+":
        x = int(input("숫자를 입력하세요"))
        y = int(input("더할 숫자를 입력하세요"))
        print(plus(x, y))
    elif calculate == "-":
        x = int(input("숫자를 입력하세요"))
        y = int(input("뺄 숫자를 입력하세요"))
        print(minus(x, y))
    elif calculate == "*":
        x = int(input("숫자를 입력하세요"))
        y = int(input("곱할 숫자를 입력하세요"))
        print(multiply(x, y))
    elif calculate == "/":
        x = int(input("숫자를 입력하세요"))
        y = int(input("나눌 숫자를 입력하세요"))
        print(divide(x, y))
    elif calculate == "종료":
        i = 0
    else:
        print("+ - * / 중 하나를 정확히 입력하세요")
