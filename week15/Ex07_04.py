# 함수 실습 p.5

def personal_info(file, search):
    def file_open():
        f = open(file, "r")
        data = f.read()
        data = data.split("\n")
        f.close()
        return data

    def name(data):
        i = 0
        lst = []
        while i < len(data):
            if "Name" in data[i]:
                dat = data[i].split(':')
                lst.append(dat[1])
            i += 1
        result = "\n".join(lst)
        print(result)


    def ex(data):
        i = 0
        name_lst = []
        age_lst = []
        phone_lst = []
        lst = []
        while i < len(data):
            if "Name" in data[i]:
                dat = data[i].split(':')
                name_lst.append(dat[1])

            if "Age" in data[i]:
                dat = data[i].split()
                age_lst.append(dat[1])

            if "Phone" in data[i]:
                dat = data[i].split()
                phone_lst.append(dat[1])
            i += 1
        i = 0
        while i < len(name_lst):
            lst.append(name_lst[i] + ": " + age_lst[i] + " /" + phone_lst[i])
            i += 1
        result = "\n".join(lst)
        print(result)

    d = file_open()
    if search == "이름":
        name(d)
    else:
        ex(d)


#personal_info("Personal_info.txt", "이름")
#personal_info("Personal_info.txt", "나이")
#personal_info("Personal_info.txt", "전화번호")
