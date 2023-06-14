"""사칙연산을 수행하는 4개의 함수를 만들기
• 입력 받는 숫자 2개
• 함수 4개의 이름
• 더하기 plus
• 빼기 minus
• 곱하기 multiply
• 나누기 divide
• 각 함수를 cal이란 리스트에 담은 후에 호출하기"""

def plus(a, b):
    return a+b
def minus(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b

cal = [plus, minus, multiply, divide]
print(cal[0](1,2))
print(cal[1](1,2))
print(cal[2](1,2))
print(cal[3](1,2))
