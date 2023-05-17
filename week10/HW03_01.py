f = open("Personal_info.txt", "r")
data = f.read()
f.close()
data = data.split('\n')
i = 0
phone_number = []
while i < len(data):
    if i % 6 == 4:
        d_2 = data[i].split()
        d = d_2[1].split('-')
        phone_number.append(d[1] + " " + d[2])
    i += 1
result = "\n".join(phone_number)

new_file = open("phone.txt", "w")
new_file.write(result)
new_file.close()
