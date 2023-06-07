# 함수 실습 p.4

def personal_info(file, search, how):
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
                lst.append(data[i])
            i += 1
        j = 0
        lst_new = []
        if how > len(lst) or how == "":
            result = "\n".join(lst)
            print(result)
        else:
            while j < how:
                lst_new.append(lst[j])
                j += 1
            result = "\n".join(lst_new)
            print(result)

    def age(data):
        i = 0
        lst = []
        while i < len(data):
            if "Age" in data[i]:
                lst.append(data[j])
            i += 1
        j = 0
        lst_new = []
        if how > len(lst) or how == "":
            result = "\n".join(lst)
            print(result)
        else:
            while j < how:
                lst_new.append(lst[j])
                j += 1
            result = "\n".join(lst_new)
            print(result)

    def phone(data):
        i = 0
        lst = []
        while i < len(data):
            if "Phone" in data[i]:
                lst.append(data[i])
            i += 1
        j = 0
        lst_new = []
        if how > len(lst) or how == "":
            result = "\n".join(lst)
            print(result)
        else:
            while j < how:
                lst_new.append(lst[i])
                j += 1
            result = "\n".join(lst_new)
            print(result)

    d = file_open()
    if search == "이름":
        name(d)
    elif search ==" 나이":
        age(d)
    elif search == "전화번호":
        phone(d)



# personal_info("Personal_info.txt", "이름", 2)
# personal_info("Personal_info.txt", "나이")
# personal_info("Personal_info.txt", "전화번호")
