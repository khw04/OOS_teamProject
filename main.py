from wordtest.wordtest import main
from quiz_prgm import main
from timer import main
from todolist.todo import main

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    while True:
        clear_screen()
        print("\n📘 기능 선택 메뉴:")
        print("1. 단어장")
        print("2. 퀴즈")
        print("3. 타이머")
        print("4. TODO 리스트")
        print("0. 종료")

        choice = input("번호 선택: ")
        if choice == "1":
            clear_screen()
            start_wordtest()
        elif choice == "2":
            clear_screen()
            start_quiz()
        elif choice == "3":
            clear_screen()
            start_timer()
        elif choice == "4":
            clear_screen()
            start_todo()
        elif choice == "0":
            print("프로그램 종료")
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main_menu()
