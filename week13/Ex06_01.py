print("''''''''''''''''''''''''''''''''")
print("학생들의 이름과 나이를 알아봅시다.")
print("''''''''''''''''''''''''''''''''")


def personal_info(file, sel):
    def file_open():
        f = open(file, "r")
        data = f.read()
        data = data.split("\n")
        f.close()
        return data

    def name(data):
        i = 0
        while i <len(data):
            if "Name" in data[i]:
                print(data[i])
            i += 1

    def age(data):
        i = 0
        while i < len(data):
            if "Age" in data[i]:
                print(data[i])
            i += 1

    d = file_open()
    if sel == "이름":
        name(d)
    elif sel =="나이":
        age(d)

personal_info("Personal_info.txt","나이")
