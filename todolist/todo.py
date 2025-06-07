# -*- coding: utf-8 -*-

from datetime import datetime # 날짜(기한) 표기용
import os # 화면 클리어용
import sys # 시스템 종료용

# -------------------------
# 화면 클리어
# -------------------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_and_clear():
    input("\n계속하려면 Enter를 누르세요...")
    clear_screen()

# -------------------------
# 할 일 생성
# -------------------------
def create_task(content, due_date_str):
    return {
        "content": content,
        "done": False,
        "due": due_date_str
    }

# -------------------------
# 할 일 삭제
# -------------------------
def delete_task(task_list, index):
    if 0 <= index < len(task_list):
        removed = task_list.pop(index)
        print(f"🗑️ '{removed['content']}' 삭제됨.")
    else:
        print("⚠️ 유효하지 않은 번호입니다.")

# -------------------------
# 완료 처리
# -------------------------
def mark_done(task_list, index):
    if 0 <= index < len(task_list):
        task_list[index]["done"] = True
        print(f"✅ '{task_list[index]['content']}' 완료 처리됨.")
    else:
        print("⚠️ 유효하지 않은 번호입니다.")

# -------------------------
# 완료 취소
# -------------------------
def mark_undone(task_list, index):
    if 0 <= index < len(task_list):
        task_list[index]["done"] = False
        print(f"↩️ '{task_list[index]['content']}' 체크 해제됨.")
    else:
        print("⚠️ 유효하지 않은 번호입니다.")

# -------------------------
# 남은 일수 계산
# -------------------------
def days_left(task):
    try:
        due_date = datetime.strptime(task["due"], "%Y-%m-%d")
        today = datetime.today()
        return (due_date - today).days
    except Exception:
        return "기한 오류"

# -------------------------
# 할 일 출력
# -------------------------
def display_tasks(task_list):
    if not task_list:
        print("\n📂 현재 등록된 할 일이 없습니다.")
        return

    print("\n📋 할 일 목록")
    for i, task in enumerate(task_list):
        status = "✔ " if task["done"] else "✘"
        if task["done"]:
            print(f"[{status}] {i+1}. {task['content']}")
        else:
            left = days_left(task)
            overdue = " (지연됨)" if isinstance(left, int) and left < 0 else ""
            print(f"[{status}] {i+1}. {task['content']} (기한: {task['due']}, 남은일수: {left}일){overdue}")

    rate = get_completion_rate(task_list)
    print(f"\n📊 달성률: {rate:.2f}%")

# -------------------------
# 달성률 (백분율로 환산)
# -------------------------
def get_completion_rate(task_list):
    total = len(task_list)
    completed = sum(1 for task in task_list if task["done"])
    return (completed / total) * 100 if total > 0 else 0

# -------------------------
# 메인 루프
# -------------------------
def main():
    task_list = []

    while True:
        clear_screen()
        print("====== TODO LIST MENU ======")
        print("1. 할 일 목록 보기")
        print("2. 할 일 추가 하기")
        print("3. 할 일 삭제 하기")
        print("4. 할 일 체크 하기")
        print("5. 할 일 체크 해제 하기")
        print("6. 프로그램 종료하기")
        print("============================")

        choice = input("번호 선택 (1-6): ").strip()

        if choice == "1":
            display_tasks(task_list)
            wait_and_clear()

        elif choice == "2":
            content = input("할 일 내용을 입력하세요: ").strip()
            due = input("기한 (YYYY-MM-DD): ").strip()
            task_list.append(create_task(content, due))
            print("🆕 추가 완료!")
            wait_and_clear()

        elif choice == "3":
            if not task_list:
                print("📂 현재 등록된 할 일이 없습니다.")
                input("Enter를 누르면 메뉴로 돌아갑니다...")
                continue
            display_tasks(task_list)
            try:
                index = int(input("삭제할 번호 입력: ")) - 1
                delete_task(task_list, index)
                wait_and_clear()
            except ValueError:
                print("⚠️ 숫자를 입력해주세요.")
                input("Enter를 누르면 메뉴로 돌아갑니다...")

        elif choice == "4":
            if not task_list:
                print("📂 현재 등록된 할 일이 없습니다.")
                input("Enter를 누르면 메뉴로 돌아갑니다...")
                continue
            display_tasks(task_list)
            try:
                index = int(input("체크할 번호 입력: ")) - 1
                mark_done(task_list, index)
                wait_and_clear()
            except ValueError:
                print("⚠️ 숫자를 입력해주세요.")
                input("Enter를 누르면 메뉴로 돌아갑니다...")

        elif choice == "5":
            if not task_list:
                print("📂 현재 등록된 할 일이 없습니다.")
                input("Enter를 누르면 메뉴로 돌아갑니다...")
                continue
            display_tasks(task_list)
            try:
                index = int(input("체크 해제할 번호 입력: ")) - 1
                mark_undone(task_list, index)
                wait_and_clear()
            except ValueError:
                print("⚠️ 숫자를 입력해주세요.")
                input("Enter를 누르면 메뉴로 돌아갑니다...")

        elif choice == "6":
            print("✅ 시스템 종료합니다. 👋")
            sys.exit()

        else:
            print("⚠️ 1~6 사이의 숫자를 입력해주세요.")
            input("Enter를 누르면 메뉴로 돌아갑니다...")

# -------------------------
# 실행 시작점
# -------------------------
if __name__ == "__main__":
    main()
