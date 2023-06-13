def cal(what, a, b):
    if what == "더하기":
        print(a+b)
    elif what == "빼기":
        print(a-b)
    elif what == "곱하기":
        print(a*b)
    elif what == "나누기":
        print(a/b)

what = input('더하기 또는 빼기 또는 곱하기 또는 나누기')
a = int(input('숫자를 입력하세요'))
b = int(input('숫자를 입력하세요'))

cal(what, a, b)
