import random
#단어 리스트 선언
word_list = ["ardvark", "baboon", "camel"]
#테스트 코드
#print(f"글자는 {word_list} 사이에서 선택 됩니다.")
#랜덤으로 리스트 에서 단어 한개 선택
chosen_word = random.choice(word_list)
#테스트 코드
#print(f"선정된 글자는 입니다.{chosen_word}")

#빈칸을 출력하기 위한 공백 리스트 선언
show_list = []
#선택된 단어의 크기만큼 반복하며 _ 표시
for char in chosen_word:
    char = "_"
    #선언된 _ 는 show_list에 추가되며 문자열 만큼 더해짐
    show_list += char
#게임을 끝내기 위한 조건 반복문 while에 들어갈 변수 선언
end_game = False
#end_game 이 False일 동안 반복
while not end_game:
    #입력을 대문자로 할수도 있으니 소문자로 전부 변환하여 입력 받는다
    chosen_user1 = input("글자를 입력하세요 : ").lower()
    #선택된 단어의 길이만큼 반복
    for answer in range(len(chosen_word)):
        #단어가 반복되는 동안 answer 를 chosen_word[]에 추가하여 word에 저장한다
        word = chosen_word[answer]
        #만약 word가 유저가 입력한 것과 동일 하다면
        if word == chosen_user1:
            #show_list리스트에 word값을 입력한다
            show_list[answer] = word
    #조건 검사가 끝나면 남은 갯수 출력
    print(show_list)
    #만약 줄13 show_list에 삽입되었던 _가 전부 유저가 입력한 word로 대체 된다면 프로그램 종료
    if "_" not in show_list:
        end_game = True
        print("전부 맞추는데 성공하였습니다!")

