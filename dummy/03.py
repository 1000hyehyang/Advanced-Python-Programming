"""• Personal_info.txt 파일 읽고, 이름만 찾아서 출력하기(절대경로)"""

file = open("C:\\Users\\ducog\\PycharmProjects\\pythonProject\\Personal_info.txt", "r")
data = file.read()
list = data.split('\n')
for i in list[:]:
    if 'Name' in i:
        arr = i.split(':')
        print(arr[1])
file.close()
