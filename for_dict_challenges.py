from collections import Counter


# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
count_names = {}
for student_name in students:
    name = student_name["first_name"]
    if name in count_names:
        count_names[name] += 1
    else:
        count_names[name] = 1
for name, count in count_names.items():
    print(f"{name}: {count}")

# student = []
# for dict_stedent in students:
#     student.append(dict_stedent['first_name'])
# count = Counter(student)


# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
print("end task -------------\n")


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
count_names = {}
for student_name in students:
    name = student_name["first_name"]
    if name in count_names:
        count_names[name] += 1
    else:
        count_names[name] = 1

most_popular_name = ""
most_popular_count = 0
for name, count in count_names.items():
    if count > most_popular_count:
        most_popular_name = name
        most_popular_count = count
print(f"Самое частое имя среди учеников: {most_popular_name}")


# Пример вывода:
# Самое частое имя среди учеников: Маша
print("end task -------------\n")

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

for class_number, class_students in enumerate(school_students, start=1):
    count_names = {}
    for student in class_students:
        name = student["first_name"]
        if name in count_names:
            count_names[name] += 1
        else:
            count_names[name] = 1
    most_popular_name = ""
    most_popular_count = 0
    for name, count in count_names.items():
        if count > most_popular_count:
            most_popular_name = name
            most_popular_count = count
    print(f"Самое частое имя в классе {class_number}: {most_popular_name}")


# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша
print("end task -------------\n")


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for class_info in school:
    count_gender_male = 0
    count_gender_female = 0
    for student in class_info['students']:
        name = student["first_name"]
        if is_male[name]:
            count_gender_male += 1
        else:
            count_gender_female += 1
    print(f"В классе {class_info['class']} {count_gender_female} девочки и {count_gender_male} мальчика.")


# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.
print("end task -------------\n")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for class_info in school:
    count_gender_male = 0
    count_gender_female = 0
    for student in class_info['students']:
        name = student["first_name"]
        if is_male[name]:
            count_gender_male += 1
            class_info['male'] = count_gender_male
        else:
            count_gender_female += 1
            class_info['female'] = count_gender_female 

for class_info in school:
    count_male = class_info.get("male", 0)
    count_female = class_info.get("female", 0)
    if count_male > count_female:
        print(f"Больше всего мальчиков в классе {class_info['class']}")
    elif count_male < count_female:
        print(f"Больше всего девочек в классе {class_info['class']}")
    else:
        print(f"В классе {class_info['class']} равное количество девочек и мальчиков")


# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a