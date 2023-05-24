# 맥도날드 kiosk에서 자신이 사용할 언어를 선택하는 상황을 가정
# “한국어” 버튼을 누르면 (입력하면) “안녕하세요” “English” 이면 “Hello”가
# 나올 수 있도록 함수 만들기

def korean():
    print("안녕하세요")
def english():
    print("Hello")

lang = input("자신이 사용할 언어를 입력하세요. 한국어 또는 English")
if lang == "한국어":
    korean()
elif lang== "English":
    english()
else:
    print("다시 입력하세요.")
