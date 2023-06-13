def plus(a, b):
    return a+b
def minus(a, b):
    return a-b
def multi(a, b):
    return a*b
def division(a, b):
    return a/b

what = input("더하기 또는 빼기 또는 곱하기 또는 나누기")
a = int(input('숫자를 입력하세요.'))
b = int(input('숫자를 입력하세요.'))

if what == "더하기":
    print(plus(a, b))
elif what == "빼기":
    print(minus(a, b))
elif what == "곱하기":
    print(multi(a, b))
elif what == "나누기":
    print(division(a, b))
