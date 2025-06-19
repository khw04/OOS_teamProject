from wordtest.wordtest import main as wordtest_main
from quiz_prgm import main as quiz_prgm_main
from timer import main as timer_main
from todolist.todo import  main as todo_main

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    while True:
        clear_screen()
        print("\n📘 기능 선택 메뉴:")
        print("1. TODO 리스트")
        print("2. 타이머")
        print("3. 단어장")
        print("4. 퀴즈")
        print("0. 종료")

        choice = input("번호 선택: ")
        if choice == "1":
            clear_screen()
            todo_main()
        elif choice == "2":
            clear_screen()
            timer_main()
        elif choice == "3":
            clear_screen()
            wordtest_main()
        elif choice == "4":
            clear_screen()
            quiz_prgm_main()
        elif choice == "0":
            print("프로그램 종료")
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main_menu()
