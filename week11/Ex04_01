# Personal_info.txt 파일 읽고, 이름만 찾아서 출력하기
with open("Personal_info.txt", "r") as f:
    data = f.read()
    data = data.split('\n')
    i = 0
    name = []
    while i < len(data):
        if i % 6 == 0:
            d_1 = data[i].split()
            d_2 = d_1[1] + " " + d_1[2]
            name.append(d_2)
        i += 1

    result = "\n".join(name)
    print(result)
