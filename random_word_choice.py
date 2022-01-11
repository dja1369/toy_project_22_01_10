import random
word_list = ["ardvark", "baboon", "camel"]
print(f"글자는 {word_list} 사이에서 선택 됩니다.")
# 프로그램 순서도
# 랜덤으로 글자를 고른다
# 유저는 글자를 맞춘다
# 글자가 들어가 있다면 어디에 있는지 출력한다
chosen_word = random.choice(word_list)
#입력을 대문자로 할수도 있으니 소문자로 전부 변환하여 입력 받는다
chosen_user1 = input("글자를 입력하세요 : ").lower()
word = ""
for letter in chosen_word:
    if letter == chosen_user1:
        print("정답입니다")
    else:
        print("틀렸습니다")


