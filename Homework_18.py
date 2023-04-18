test_design_writers = ["Smith", "Harakiri", "Olen"]
scripters = ["Tom", "Olen", "Kate", "Tobi"]
reviewers = ["Smith", "Volk", "Anunah"]
out_of_office_today = ["Olen", "Tobi"]

test_design_writers = [1, 3, 5]

scripters = [2, 3, 4, 6, 7, 8]

reviewers = [1, 2, 3, 9, 10]

out_of_office_today = [2, 5, 6, 1]

# всех тестировщиков в команде
all_testers = sorted(set(test_design_writers) | set(scripters) | set(reviewers))

print("All testers in the team:")
print(all_testers)

# тестировщики, которые могут только писать скрипты
scripters_only = sorted(set(scripters) - set(test_design_writers) - set(reviewers))

print("\nTesters who can only write scripts:")
print(scripters_only)

# тестировщики, которые сегодня на работе
working_today = sorted(set(all_testers) - set(out_of_office_today))

print("\nTesters working today:")
print(working_today)

# тестировщики, которые могут писать и ревьюить скрипты, и которые сегодня на работе
scripters_reviewers_working = sorted(set(scripters) & set(reviewers) & set(working_today))

print("\nTesters who can write and review scripts and are working today:")
print(scripters_reviewers_working)

