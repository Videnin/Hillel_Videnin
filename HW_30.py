from datetime import datetime, timedelta

start_date = datetime(2023, 3, 27, 19, 15)

lecture_days = [0, 3]  # 0 - понедельник, 3 - четверг

num_lectures = 32

# генерируем список дат
lecture_dates = [start_date]
while len(lecture_dates) < num_lectures:
    next_date = lecture_dates[-1] + timedelta(days=1)
    if next_date.weekday() in lecture_days:
        lecture_dates.append(next_date)

for i, lecture_date in enumerate(lecture_dates):
    print(f"Lecture {i+1:2d}: {lecture_date:%d %b %Y %H:%M}")
