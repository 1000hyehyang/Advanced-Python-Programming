""" • jumin_list = ['950101-1234567', '891230-2345678', '010101-
3456789', '800101-4567890', '721010-5678901', '660101-6789012',
'030202-7890123', '480101-8901234', '051231-9012345', '980101-
0123456’]
• 올바른 주민번호만 출력하기, continue 이용하기
• 올바르지 않은 주민번호(7번째 숫자가 1,2,3,4가 아니면)는 삭제하기, pass 이용하기"""

jumin_list = ['950101-1234567', '891230-2345678', '010101-3456789', '800101-4567890', '721010-5678901', '660101-6789012',
'030202-7890123', '480101-8901234', '051231-9012345', '980101-0123456']

for i in jumin_list:
    if i[7] not in ['1', '2', '3', '4']:
        continue
    print(i)

print("'''''''''''''''''''''")

for i in jumin_list[:]:
    if i[7] not in ['1', '2', '3', '4']:
        jumin_list.remove(i)
        pass
    else:
        print(i)
