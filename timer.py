import time
import json
import os
from datetime import datetime, timedelta
from collections import defaultdict

class StudyTracker:
    def __init__(self):
        self.start_time = None
        self.sessions = []
        self.today_date = datetime.now().date()
        self.data_file = "study_data.json"
        self.load_data()
        
    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}
            
    def save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2, default=str)
