import time
import json
import os
from datetime import datetime, timedelta
from collections import defaultdict

class StudyTracker:  # 공부 타이머 클래스
    def __init__(self):
        self.start_time = None                          # 시작 시간 저장
        self.sessions = []                              # 공부 세션 저장 리스트
        self.today_date = datetime.now().date()         # 오늘 날짜
        self.data_file = "study_data.json"              # 저장할 파일 이름
        self.load_data()                                # 기존 데이터 불러오기

    def load_data(self):  # 기존 데이터 불러오기
        try:
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}

    def save_data(self):  # 현재 데이터 저장
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2, default=str)

    def start(self):  # 공부 시작
        self.start_time = time.time()
        print("⏱️ 공부 시작!")
        input("엔터를 눌러 계속하세요...")

    def pause(self, token):  # 공부 중지 및 기록
        if self.start_time is None:
            print("⚠️ 아직 시작하지 않았습니다.")
            input("엔터를 눌러 계속하세요...")
            return
        end_time = time.time()
        duration = end_time - self.start_time
        self.sessions.append((self.start_time, end_time, token))
        print(f"⏸️ 중지됨 - {token} 공부시간: {timedelta(seconds=duration)}")
        input("엔터를 눌러 계속하세요...")
        self.start_time = None

    def end_day(self):  # 당일 공부 기록 저장
        today_str = str(self.today_date)
        if today_str not in self.data:
            self.data[today_str] = []

        for start, end, token in self.sessions:
            self.data[today_str].append({
                "start": start,
                "end": end,
                "token": token,
                "duration": end - start
            })
        self.save_data()
        print("✅ 오늘 공부 기록 저장 완료.")
        input("엔터를 눌러 계속하세요...")

    def show_summary(self):  # 하루 공부 요약
        today_str = str(self.today_date)
        if today_str not in self.data:
            print("오늘 공부 기록이 없습니다.")
            input("엔터를 눌러 계속하세요...")
            return

        total = 0
        token_map = defaultdict(float)

        for record in self.data[today_str]:
            duration = record['duration']
            token = record['token']
            total += duration
            token_map[token] += duration

        print(f"\n📅 {today_str} 공부 요약")
        print(f"총 공부 시간: {timedelta(seconds=total)}")
        for token, sec in token_map.items():
            print(f"  {token}: {timedelta(seconds=sec)}")
        print("💡 휴식은 총 공부 시간의 20% 정도를 추천합니다.\n")
        input("엔터를 눌러 계속하세요...")

def clear_screen():  # 화면 지우기 (Windows)
    os.system('cls' if os.name == 'nt' else 'clear')

def main():  # 메인 루프
    tracker = StudyTracker()

    while True:
        clear_screen()
        print("\n==== 공부 시간 측정기 ====")
        print("1. 공부 시작")
        print("2. 공부 중지")
        print("3. 오늘 요약 보기")
        print("4. 기록 저장 (종료)")
        print("5. 메인 시작 화면으로 돌아가기")

        choice = input("선택하세요 (1-5): ")

        if choice == '1':
            tracker.start()
        elif choice == '2':
            token = input("어떤 과목(토큰)인가요? ")
            tracker.pause(token)
        elif choice == '3':
            tracker.show_summary()
        elif choice == '4':
            tracker.end_day()
        elif choice == '5':
            print("프로그램을 종료합니다.")
            return 1
        else:
            print("올바른 번호를 입력해 주세요.")

if __name__ == "__main__":  # 시작 지점
    main()
