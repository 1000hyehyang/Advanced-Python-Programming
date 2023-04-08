data = ''' "You don't have to be French to enjoy a decent red wine," Charles
Jousselin de Gruse used to tell his foreign guests whenever he
entertained them in Paris. "But you do have to be French to
recognize one," he would add with a laugh.

After a lifetime in the French diplomatic corps, the Count de Gruse
lived with his wife in an elegant townhouse on Quai Voltaire. He was
a likeable man, cultivated of course, with a well-deserved reputation
as a generous host and an amusing raconteur.

This evening's guests were all European and all equally convinced
that immigration was at the root of Europe's problems. Charles de
Gruse said nothing. He had always concealed his contempt for such
ideas. And, in any case, he had never much cared for these
particular guests.…'''

# 처음으로 등장한 단어 of를 in으로 바꾸기 (문법성 x)
pre_data_list = data.split()                # pre_data_list에 data의 문자열을 공백으로 구분하여 나누어주면 단어 단위로 쪼개어 집니다. 이때 don't와 같은 준말은 한 단어로 간주합니다.
of_location = pre_data_list.index('of')     # 먼저 of의 위치를 찾습니다.
pre_data_list.remove('of')                  # 처음 등장하는 of를 삭제합니다.
pre_data_list.insert(of_location, 'in')     # 원래 있던 of 자리에 in을 삽입합니다.
new_data = " ".join(pre_data_list)          # 리스트로 되어 있는 data를 새로운 문자열로 만들어줍니다.
print('#4. data에서 처음 등장한 of를 in으로 바꾸면 다음과 같습니다.')       # 완벽하게 문제를 풀기 위해 임의로 문제의 순서를 바꾸었습니다.
print(new_data)

# 문제 풀이 전 data 조작하기
data = data.replace("\"","")        # data에 있는 문장부호 "를 삭제해줍니다. 그래야 다음 문제를 풀 때 수월해집니다.
data = data.replace(",","")         # 마찬가지로 ,도 삭제해줍니다.
data = data.replace(".","")         # 마찬가지로 .도 삭제해줍니다.

# 전체 단어 수 구하기
data_list = data.split()    # data_list에 data의 문자열을 공백으로 구분하여 나누어주면 단어 단위로 쪼개어 집니다. 이때 don't와 같은 준말은 한 단어로 간주합니다.
word_number = len(data_list)
print('#1. 전체 단어 수는 {}입니다.'.format(word_number))

# 단어 he가 몇 번 등장하는지 구하기
how_he = data_list.count("he")  # he와 He는 다른 것으로 구분됩니다. 따라서 He는 따로 더 구해주어 합해야 합니다.
how_He = data_list.count("He")  # 저는 'he'라는 두 글자 문자가 아니라 '그'라는 뜻을 지닌 단어 'he(He)'를 구하는 것으로 이해했습니다.
total = how_he + how_He
print('#2. he는 총 {}번 등장합니다.'.format(total))

# 한 줄에 한 단어씩 넣어 하나의 문자열에 담기
new_string = "\n".join(data_list)
print('#3. new_string 변수에 한 줄에 한 단어씩 넣으면 다음과 같습니다.')
print(new_string)


# 열 번째 단어 추출하고 출력하기
tenth_word = data_list[9]
print('#5. 열 번째 단어는 "{}" 입니다.'.format(tenth_word))

# 오름차순으로 정렬한 단어 목록 만들기
data_list.sort()
print("#6. 오름차순으로 정리한 단어 목록은 다음과 같습니다.")
print(data_list)
