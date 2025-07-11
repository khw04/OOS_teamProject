import json
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


FILE_NAME = "voca.json"

# 사용자 불러오기(없으면 생성)
def get_username(username):
    return f"{username}_voca.json"

# 단어장 파일 불러옴
def load_voca(username):  # 저장한 파일 불러옴, 없으면 빈 파일 리턴
    filename = get_username(username)
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

# 단어 저장
def save_voca(username, voca):
    filename = get_username(username)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(voca, f, ensure_ascii=False, indent=2)

# 단어 추가 
def add_word(voca):
    word = input("영단어 입력: ").strip()
    meaning = input("한글 뜻 입력: ").strip()
    voca[word] = {"meaning": meaning, "correct": 0, "wrong": 0}
    print("추가되었습니다!")

# 저장한 단어 출력
def view_words(voca):
    if not voca:
        print("저장된 단어가 없습니다.")
        return

    print("\n--- 단어 목록 ---")
    for i, (word, data) in enumerate(voca.items(), start=1):
        print(f"{i}. {word} = {data['meaning']}")

# 퀴즈
def quiz(voca):
    if not voca:  # 단어 없을 때 출력
        print("단어가 없습니다. 먼저 단어를 추가하세요.")
        return
    
    print("퀴즈를 시작합니다. 종료하려면 'exit'을 입력하세요.\n")

    while True: # 사용자가 따로 종료할 때 까지 무한루프(정답 및 틀릿 횟수 영향 x)
        word = random.choice(list(voca.keys()))
        data = voca[word]
        meaning = data["meaning"]
        mode = random.choice(['word', 'meaning'])  # 랜덤으로 출제 (영어 스펠링 or 한글 뜻 랜덤)

        if mode == 'word':
            print(f"뜻: {meaning}")
            answer = input("영어 단어 입력 (종료하려면 exit 입력): ").strip()
            if answer.lower() == 'exit':
                print("퀴즈를 종료합니다.")
                break
            if answer.lower() == word.lower():
                print("정답입니다!")
            else:
                print(f"틀렸습니다. 정답은: {word}")
        else:
            print(f"단어: {word}")
            answer = input("한글 뜻 입력 (종료하려면 exit 입력): ").strip()
            if answer.lower() == 'exit':
                print("퀴즈를 종료합니다.")
                break
            if answer == meaning:
                print("정답입니다!")
            else:
                print(f"틀렸습니다. 정답은: {meaning}")

# 단어 시험하기
def word_test(voca):
    if not voca:
        print("단어장이 비어있습니다.")
        return

    print("\n[단어 시험]")
    print("1. 새 단어 또는 오답 없는 단어")
    print("2. 1회 이상 틀린 단어")
    print("3. 3회 이상 틀린 단어")
    mode = input("난이도 선택 (1/2/3): ").strip()

    # 조건에 맞는 단어 불러오기
    if mode == '1':
        selected = [word for word, data in voca.items() if data["wrong"] == 0]
    elif mode == '2':
        selected = [word for word, data in voca.items() if data["wrong"] >= 1]
    elif mode == '3':
        selected = [word for word, data in voca.items() if data["wrong"] >= 3]
    else:
        print("잘못된 선택입니다.")
        return

    if not selected:
        print("조건에 맞는 단어가 없습니다.")
        return

    questions = random.sample(selected, min(30, len(selected)))

    for word in questions:
        data = voca[word]
        if random.choice(['word', 'meaning']) == 'word':
            print(f"\n뜻: {data['meaning']}")
            answer = input("영단어 입력 (종료하려면 exit 입력): ").strip()
            if answer.lower() == 'exit':
                break
            elif answer.lower() == word.lower():
                print("정답입니다!")
                data['correct'] += 1
            else:
                print(f"틀렸습니다. 정답은: {word}")
                data['wrong'] += 1
        else:
            print(f"\n단어: {word}")
            answer = input("한글 뜻 입력 (종료하려면 exit 입력): ").strip()
            if answer.lower() == 'exit':
                break
            elif answer == data['meaning']:
                print("정답입니다!")
                data['correct'] += 1
            else:
                print(f"틀렸습니다. 정답은: {data['meaning']}")
                data['wrong'] += 1

    # 5회 이상 맞힌 단어 삭제
    to_delete = [word for word, data in voca.items() if data['correct'] >= 5]
    for word in to_delete:
        print(f"'{word}'는 5회 이상 맞혀 삭제되었습니다.")
        del voca[word]

# 단어 삭제
def delete_word(voca):
    word = input("삭제할 영단어 입력: ").strip()
    if word in voca:
        confirm = input(f"정말로 '{word}'를 삭제하시겠습니까? (y/n): ").strip().lower()
        if confirm == 'y':
            del voca[word]
            print(f"'{word}'가 삭제되었습니다.")
        else:
            print("삭제가 취소되었습니다.")
    else:
        print(f"'{word}'는 단어장에 없습니다.")

# 메인 함수
def main():
    username = input("사용자 이름을 입력하세요: ").strip()
    voca = load_voca(username)

    while True:
        clear_screen()
        print("\n--- 단어 암기장 ---")
        print("1. 단어 추가")
        print("2. 단어 보기")
        print("3. 퀴즈 풀기(1개씩 반복 학습)")
        print("4. 단어 시험하기(최대 30개)")
        print("5. 단어 삭제")
        print("6. 메인 시작 화면으로 돌아가기")
        choice = input("선택: ").strip()

        if choice == '1':
            add_word(voca)
            save_voca(username, voca)
        elif choice == '2':
            view_words(voca)
        elif choice == '3':
            quiz(voca)
        elif choice == '4':
            word_test(voca)
            save_voca(username, voca)
        elif choice == '5':
            delete_word(voca)
            save_voca(username, voca)
        elif choice == '6':
            print("프로그램 종료.")
            return 1
        else:
            print("올바른 번호를 입력하세요.")

if __name__ == "__main__":
    main()