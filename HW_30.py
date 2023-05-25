import datetime

start_date = datetime.date(2023, 3, 27)  # Дата первого занятия
num_lectures = 20  # Количество занятий

lecture_time = datetime.time(19, 15)  # Время занятий
lecture_days = [0, 3]  # Понедельник (0) и четверг (3)

lectures = []

current_date = start_date
for i in range(num_lectures):
    while current_date.weekday() not in lecture_days:
        current_date += datetime.timedelta(days=1)
    lecture_datetime = datetime.datetime.combine(current_date, lecture_time)
    lectures.append(lecture_datetime)
    current_date += datetime.timedelta(days=1)

# Вывод списка занятий
for i, lecture in enumerate(lectures, start=1):
    lecture_number = str(i).rjust(2)
    lecture_date = lecture.date().strftime('%d.%m.%Y')
    lecture_time = lecture.time().strftime('%H:%M')
    print(f"Лекция {lecture_number}: {lecture_date}, {lecture_time}")
