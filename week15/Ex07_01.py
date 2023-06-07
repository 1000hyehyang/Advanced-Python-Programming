# 함수 실습 p.2

def personal_info(file, save, search):
    def file_open():
        f = open(file, "r")
        data = f.read()
        data = data.split("\n")
        f.close()
        return data

    def name(data):
        i = 0
        lst = []
        while i <len(data):
            if "Name" in data[i]:
                lst.append(data[i])
            i += 1
        result = "\n".join(lst)
        f1 = open(save, "w")
        f1.write(result)
        f1.close()

    def age(data):
        i = 0
        lst = []
        while i < len(data):
            if "Age" in data[i]:
                lst.append(data[i])
            i += 1
        result = "\n".join(lst)
        f1 = open(save, "w")
        f1.write(result)
        f1.close()

    def phone(data):
        i = 0
        lst = []
        while i < len(data):
            if "Phone" in data[i]:
                lst.append(data[i])
            i += 1

        result = "\n".join(lst)
        f1 = open(save, "w")
        f1.write(result)
        f1.close()

    d = file_open()

    if search == "이름":
        name(d)
    elif search =="나이":
        age(d)
    elif search == "전화번호":
        phone(d)

# personal_info("Personal_info.txt", "extract_info.txt", "이름")
# personal_info("Personal_info.txt","extract_info.txt", "나이")
# personal_info("Personal_info.txt","extract_info.txt", "전화번호")
