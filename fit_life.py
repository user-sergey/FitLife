# Проект FitLife - MVP версия 1.1

WATER_PER_KG = 30
ML_PER_LITER = 1000


def define_a_word_for_age(age):
    """Определение слова, которое будет напечатано в отчёте после возраста."""
    if 11 <= age % 100 <= 14:
        word = 'лет'
    elif age % 10 == 1:
        word = 'год'
    elif 2 <= age % 10 <= 4:
        word = 'года'
    else:
        word = 'лет'
    return word


def interpret_the_value_of_bmi(bmi, age):
    """Интерпретация вычисленного индекса массы тела."""
    if age >= 18:
        descriptions_of_bmi = [
            (16.0, 'выраженный дефицит массы тела'),
            (18.5, 'недостаточная масса тела (дефицит)'),
            (25.0, 'нормальная масса тела'),
            (30.0, 'избыточная масса тела (предожирение)'),
            (35.0, 'ожирение 1-й степени'),
            (40.0, 'ожирение 2-й степени'),
            (float('inf'), 'ожирение 3-й степени')
        ]
    elif 12 < age < 18:
        descriptions_of_bmi = [
            (16.0, 'недостаточная масса тела'),
            (24.0, 'нормальная масса тела'),
            (float('inf'), 'избыточная масса тела')
        ]
    elif 5 < age <= 12:
        descriptions_of_bmi = [
            (14.0, 'недостаточная масса тела'),
            (20.0, 'нормальная масса тела'),
            (float('inf'), 'избыточная масса тела')
        ]
    else:
        descriptions_of_bmi = [
            (13.5, 'недостаточная масса тела'),
            (18.0, 'нормальная масса тела'),
            (float('inf'), 'избыточная масса тела')
        ]
    final_assessment = ''
    for number, text in descriptions_of_bmi:
        if bmi < number:
            final_assessment = text
            break
    return final_assessment


print('Здравствуйте! Я бот FitLife.')
while True:
    user_name = input('Напишите, пожалуйста, как Вас зовут? ').strip()
    if user_name:
        break
    print('Имя не может быть пустым! Пожалуйста, повторите ввод.')

while True:
    try:
        user_age = int(input('Ваш возраст? (вводите только число): '))
        if user_age < 2:
            print('Этот калькулятор предназначен для лиц от 2 лет и старше! '
                  'Пожалуйста, введите другое числовое значение возраста.')
        elif user_age > 150:
            print('Неверное значение! '
                  'Пожалуйста, введите реальный возраст (не более 150 лет).')
        else:
            break
    except ValueError:
        print('Некорректный ввод! '
              'Пожалуйста, введите целое число (например, 25).')

while True:
    try:
        user_weight = float(input('Введите Ваш вес '
                                  '(в килограммах, например, 45.5): '))
        if user_weight <= 5 or user_weight >= 500:
            print('Неверное значение! Пожалуйста, введите реальный вес '
                  'в килограммах (больше 5 и меньше 500 кг).')
        else:
            break
    except ValueError:
        print('Некорректный ввод! '
              'Пожалуйста, введите целое число (например, 45) '
              'или дробное, используя точку (например, 45.4).')

while True:
    try:
        user_height = float(input('Введите Ваш рост '
                                  '(в метрах, например, 1.62): '))
        if user_height >= 4 or user_height <= 0.5:
            print('Неверное значение! Пожалуйста, введите реальный рост '
                  'в метрах (больше 0.5 и меньше 4 м, '
                  'например: 1.5, 1.75, 2).')
        else:
            break
    except ValueError:
        print('Некорректный ввод! '
              'Пожалуйста, введите значение в метрах '
              '(например: 1.5, 1.75, 2).')

# Расчёт индекса массы тела и его оценка.
body_mass_index = round(user_weight / (user_height ** 2), 1)
description_of_bmi = interpret_the_value_of_bmi(body_mass_index, user_age)

# Расчёт суточной нормы воды.
water_norm_in_ml = user_weight * WATER_PER_KG
water_norm_in_liters = round(water_norm_in_ml / ML_PER_LITER, 1)

# Печать отчёта.
word_for_age = define_a_word_for_age(user_age)
print(f'\nОтчёт для пользователя: {user_name} ({user_age} {word_for_age})')
print(f'\nВаш индекс массы тела: {body_mass_index}.')
if user_age >= 18:
    print(f'\nСогласно рекомендациям ВОЗ, у Вас {description_of_bmi}.')
else:
    print(f'\nУ Вас {description_of_bmi}.')
    print('Внимание! В Вашем возрасте организм ещё формируется, '
          'поэтому оценка может быть неточной.\nРекомендуется сверять индекс '
          'массы тела с региональными центильными таблицами у педиатров.')
print(f'\nРекомендуемая норма воды: {water_norm_in_liters} л в день.')
print('\nРасчёт окончен. Будьте здоровы!')
