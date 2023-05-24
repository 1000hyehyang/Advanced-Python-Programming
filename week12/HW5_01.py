# 사용자 정의 함수 만들 것
# 1. 파일 열고 읽는 함수 (자주 사용하는 것이니 개별적으로 1개 만들기)
# 2. 데이터를 가공하는 함수(함수 개수 자유롭게)
# 이름: 평균점수 형태로 출력될 수 있도록 만들기

def read():
    f = open("score.txt", "r")
    data = f.read()
    return data
    f.close()

def arrange(data):
    new_data = data.split('\n')
    results = []
    for line in new_data:
        d = line.split(' ')
        for i in range(len(d)):
            if ',' in d[i]:
                d[i] = d[i].replace(',', '')
        name = d[0]
        average = (int(d[3]) + int(d[5]) + int(d[7]))/3
        result = f"{name}: {average}"
        print(result)
        results.append(result)
    return results


print("''''''''''''''''''''''''''''''''")
print("학생들의 이름과 평균 점수를 알아봅시다.")
print("''''''''''''''''''''''''''''''''")

data = read()
arrange(data)
#results = arrange(data)


# 파일에 쓰는 함수도 만들기 [파일이 생성되지 않도록 하라고 하셨기에 주석처리합니다.]
#def write(data):
#    f1 = open("score_av.txt", "w")
#    f1.write(data)
#    f1.close()

#write_data = '\n'.join(results)
#write(write_data)
