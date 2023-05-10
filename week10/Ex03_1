file = open("Personal_info.txt", "r")
data = file.read()
file.close()
data = data.split('\n')     # 한 줄씩 데이터를 나눠준다.
i = 0
while i < len(data):    # 각 줄 마다 조건을 확인해준다.
    if i % 6 == 0:     # 0, 6, 12, 18, 24번째 줄에 이름이 존재하므로
        d = data[i].split()     # 이름이 존재하는 줄이라면 데이터를 공백으로 나누어 준다
        name = d[1] + " " + d[2]    # 성과 이름을 합쳐준다
        print(name)
    i += 1  
