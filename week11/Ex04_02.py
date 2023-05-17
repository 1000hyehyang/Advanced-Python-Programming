# 2번 문제
i = 2
j = 2

while i <= 4:
    if j != 5:
        data = i ** j
        print("{}의 {}의 제곱: {}".format(i, j, data))
        j += 1
    else:
        i += 1
        j = 2
