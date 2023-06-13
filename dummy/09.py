def lets(*text, sep):
    text = list(text)
    text = sep.join(text)
    print(text)

lets("a", "b", "c", sep = '\n')
# 가변 - 일반 순서로 사용하기 위해서는 호출할 때 일반을 반드시 기본값 매개변수로 입력해야 함.
