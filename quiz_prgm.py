import json
import random

def load_answer_sheet(filename):  # 답안지(json파일) 불러오기
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_answer_sheet(filename, answer_sheet):  # 답안지(json파일) 쓰기
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(answer_sheet, f, ensure_ascii=False, indent=4)

def add_quiz():  # 퀴즈 저장하기 (객관식, 주관식, OX)
    question = input("문제: ").strip()
    while True:
        qtype = input("유형 (객관식/주관식/OX): ").strip().upper()
        if qtype in ("객관식", "주관식", "OX"):
            break
        print("객관식, 주관식 또는 OX만 입력 가능합니다.")

    quiz = {
        "question": question,
        "type": qtype
    }

    if qtype == "객관식":
        choices = []
        print("객관식 선택지 4개를 입력하세요.")
        for i in range(4):
            while True:
                choice = input(f"선택지 {i+1}: ").strip()
                if choice:
                    choices.append(choice)
                    break
                print("빈 입력은 안 됩니다.")
        quiz["choices"] = choices

    elif qtype == "OX":
        quiz["choices"] = ["O", "X"]

    answer = input("정답을 입력하세요: ").strip()
    quiz["answer"] = answer

    return quiz

def delete_quiz(answer_sheet, filename):
    if not answer_sheet:
        print("삭제할 퀴즈가 없습니다.")
        return

    print("\n=== 삭제할 퀴즈 목록 ===")
    for idx, quiz in enumerate(answer_sheet, 1):
        print(f"{idx}. {quiz['question']}")

    while True:
        choice = input("삭제할 퀴즈 번호를 입력하세요 (취소: 0): ").strip()
        if choice.isdigit():
            idx = int(choice)
            if idx == 0:
                print("삭제를 취소했습니다.")
                return
            if 1 <= idx <= len(answer_sheet):
                removed = answer_sheet.pop(idx - 1)
                save_answer_sheet(filename, answer_sheet)
                print(f"'{removed['question']}' 퀴즈가 삭제되었습니다.")
                return
        print("올바른 번호를 입력하세요.")

def run_quiz(quiz):
    print("\n문제:", quiz["question"])
    if quiz["type"] in ("객관식", "OX"): #객관식, OX
        for idx, choice in enumerate(quiz["choices"], 1):
            print(f"{idx}. {choice}")
        while True:
            ans = input("정답 번호를 입력하세요: ").strip()
            if ans.isdigit():
                ans_idx = int(ans) - 1
                if 0 <= ans_idx < len(quiz["choices"]):
                    if quiz["choices"][ans_idx].strip().lower() == quiz["answer"].strip().lower():
                        print("정답입니다!")
                    else:
                        print(f"틀렸습니다. 정답은 '{quiz['answer']}'입니다.")
                    break
            print("올바른 번호를 입력하세요.")
    else:  # 주관식
        ans = input("정답을 입력하세요: ").strip()
        if ans.strip().lower() == quiz["answer"].strip().lower():
            print("정답입니다!")
        else:
            print(f"틀렸습니다. 정답은 '{quiz['answer']}'입니다.")

def main(): #메인함수, exit 하기전까지 남기기
    filename = "answer_sheet.json"
    answer_sheet = load_answer_sheet(filename)

    while True: 
        print("\n=== 퀴즈 프로그램 ===")
        print("1. 퀴즈 추가")
        print("2. 퀴즈 실행")
        print("3. 퀴즈 삭제제")
        print("4. 종료")
        choice = input("선택: ").strip()

        if choice == "1":
            quiz = add_quiz()
            answer_sheet.append(quiz)
            save_answer_sheet(filename, answer_sheet)
            print("퀴즈가 저장되었습니다.")
        elif choice == "2":
            if not answer_sheet:
                print("등록된 퀴즈가 없습니다.")
                continue
            shuffled_sheet = answer_sheet[:]
            random.shuffle(shuffled_sheet)
            for quiz in shuffled_sheet:
                run_quiz(quiz)
        elif choice == "3":
            delete_quiz(answer_sheet, filename)
        elif choice == "4":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__": #메인함수 실행
    main()
