a = [1, 2, 3, 4, 5]
f = open("write_1.txt", "w")
f.write(str(a))
f.close()
print("'''''''''''''''''''''''''''")
f_2 = open("write_2.txt", "w")
i = 0
while i <len(a):
    a[i] = str(a[i]) + " "
    i += 1
f_2.writelines(a)
f_2.close()
