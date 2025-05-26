# models/modelo_sueno.py
class SleepAnalyzer:
    def __init__(self, user_id, sleep_data):
        self.user_id = user_id
        self.sleep_data = sleep_data

    def average_sleep_hours(self):
        total = sum(d['total_sleep_hours'] for d in self.sleep_data)
        return total / len(self.sleep_data)

    def detect_problems(self):
        issues = []
        for d in self.sleep_data:
            if d['sleep_quality'] < 50 or d['awake_count'] > 3:
                issues.append((d['date'], d['sleep_quality'], d['awake_count']))
        return issues
