"""• a ="We're studying for loop“
• 단어 단위로 분할하고, 한 단어씩 출력
• 문자 길이(개수)도 함께 출력
줄 번호도 추가해서 함께 출력
• 예) 1. We’re: 5 / 2. studying: 8"""

a = "We're studying for loop"
list = a.split()
for i in range(len(list)):
    print(i+1, ".", list[i],':', len(list[i]))
