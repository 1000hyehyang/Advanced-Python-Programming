"""• print_POS(love='verb', computer='noun', paper='noun’, 
pretty='adjective’)
• 위의 형태로 함수를 호출하고 아래와 같이 출력될 수 있도록 함수를 정의하기
love: verb
computer: noun
paper: noun
pretty: adjective"""

def pos(**words):
    key = []
    value = []
    for i in words:
        key.append(i)
    for i in words.values():
        value.append(i)
    for i in range(len(words)):
        print(f'{key[i]} : {value[i]}')

pos(love='verb', computer='noun', paper='noun', pretty= 'adjective')
