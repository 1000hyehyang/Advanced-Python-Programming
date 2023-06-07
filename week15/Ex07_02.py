# 함수 실습 p.3

def file_open(file):
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
    print(result)

def age(data):
    i = 0
    lst = []
    while i < len(data):
        if "Age" in data[i]:
            lst.append(data[i])
        i += 1
    result = "\n".join(lst)
    print(result)

def phone(data):
    i = 0
    lst = []
    while i < len(data):
        if "Phone" in data[i]:
            lst.append(data[i])
        i += 1
    result = "\n".join(lst)
    print(result)

def call_def(file, search):
    data = file_open(file)

    if search == "이름":
        name(data)
    elif search == "나이":
        age(data)
    elif search == "전화번호":
        phone(data)

# call_def("Personal_info.txt", "이름")
# call_def("Personal_info.txt", "나이")
# call_def("Personal_info.txt", "전화번호")
