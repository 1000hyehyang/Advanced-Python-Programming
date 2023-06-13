def kiosk(language):
    if language == "한국어":
        print("안녕하세요")
    elif language == "English":
        print("Hello")

language = input('한국어 또는 English를 입력하세요.')
kiosk(language)
