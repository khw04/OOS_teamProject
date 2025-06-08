import json
import random
import os

FILE_NAME = "voca.json"

# 단어장 파일 불러옴
def load_voca(): # 2(2). 저장한 파일 불러옴, 없으면 빈 파일 리턴
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

# 단어 저장
def save_voca(voca):
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(voca, f, ensure_ascii=False, indent=2) #json 파일에 단어 저장장

# 단어 추가 
def add_word(voca): # 키 값 저장해서 넘김
    word = input("단어: ").strip()
    meaning = input("뜻: ").strip()
    voca[word] = meaning
    print("추가되었습니다!")

# 저장한 단어 출력
def view_words(voca):
    if not voca:
        print("저장된 단어가 없습니다.")
        return
    
    print("\n--- 단어 목록 ---")
    for word, meaning in voca.items():
        print(f"{word} : {meaning}")
    print()

# 퀴즈
def quiz(voca):
    if not voca: # 단어 없을 때 출력
        print("단어가 없습니다. 먼저 단어를 추가하세요.")
        return
    
    word, meaning = random.choice(list(voca.items()))
    mode = random.choice(['word', 'meaning'])  # 랜덤으로 출제 (영어 스펠링 or 한글 뜻 랜덤으로 물어봄)

    if mode == 'word':
        print(f"뜻: {meaning}")
        answer = input("영어 단어 입력: ").strip()
        if answer.lower() == word.lower(): # lower = 대문자 전부 소문자로 (대소문자 구분 x)
            print("정답입니다!")
        else:
            print(f"틀렸습니다. 정답은: {word}")
    else:
        print(f"단어: {word}")
        answer = input("뜻 입력: ").strip()
        if answer == meaning:
            print("정답입니다!")
        else:
            print(f"틀렸습니다. 정답은: {meaning}")

# 메인
def main(): # 1. 메인 함수 실행
    voca = load_voca() # 2. 단어 저장한 파일 불러옴
    while True: # 3. 무한 루프 (기능 보여주고 각 기능 실행함)
        print("\n--- 단어 암기장 ---")
        print("1. 단어 추가")
        print("2. 단어 보기")
        print("3. 퀴즈 풀기")
        print("4. 종료")
        choice = input("선택: ").strip()

        if choice == '1': # 단어 추가 후 저장
            add_word(voca)
            save_voca(voca)
        elif choice == '2': # 단어장에 저장 된 모든 단어 출력 (스펠링, 뜻 같이 출력됨)
            view_words(voca)
        elif choice == '3': # 단어장에서 랜덤으로 단어 선택 후 퀴즈
            quiz(voca)
        elif choice == '4': # 종료료
            print("프로그램 종료.")
            break
        else:
            print("올바른 번호를 입력하세요.")

if __name__ == "__main__":
    main()