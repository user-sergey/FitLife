# Проект FitLife - MVP версия 1.2.

import sys

WATER_PER_KG = 30
ML_PER_LITER = 1000


def check_before_exiting_the_program(field):
    """Проверка до выхода из программы по желанию пользователя."""
    entered_value = input('Выйти? Нажмите Enter. Чтобы продолжить, '
                          f'введите {field}, после нажмите Enter: ').strip()
    if not entered_value:
        print('\nРабота программы завершена. Всего доброго!\n')
        sys.exit()
    else:
        return entered_value


def enter_and_process_numerical_data(
        name_for_field,
        min_value,
        max_value,
        strict,
        range_error,
        type_error,
        converter
):
    """Ввод и обработка числовых данных (возраст, вес, рост)."""
    while True:
        if name_for_field == 'возраст':
            entered_value = input('Ваш возраст? '
                                  '(вводите только число): ').strip()
        elif name_for_field == 'вес':
            entered_value = input('Введите Ваш вес '
                                  '(в килограммах, например, 45.5): ').strip()
        else:
            entered_value = input('Введите Ваш рост '
                                  '(в метрах, например, 1.62): ').strip()
        if not entered_value:
            entered_value = check_before_exiting_the_program(name_for_field)

        try:
            if converter is int:
                value = int(entered_value)
            else:
                value = float(entered_value)

            if strict:
                in_range = min_value < value < max_value
            else:
                in_range = min_value <= value <= max_value

            if in_range:
                return value
            print(range_error)
        except ValueError:
            print(type_error)


def interpret_the_value_of_bmi(bmi, age):
    """Интерпретация вычисленного индекса массы тела."""
    if age >= 18:
        descriptions_of_bmi = [
            (16.0, 'выраженный дефицит массы тела'),
            (18.5, 'недостаточная масса тела (дефицит)'),
            (25.0, 'нормальная масса тела'),
            (30.0, 'избыточная масса тела (предожирение)'),
            (35.0, 'ожирение 1-й степени'),
            (40.0, 'ожирение 2-й степени')
        ]
    elif age > 12:
        descriptions_of_bmi = [
            (16.0, 'недостаточная масса тела'),
            (24.0, 'нормальная масса тела')
        ]
    elif age > 5:
        descriptions_of_bmi = [
            (14.0, 'недостаточная масса тела'),
            (20.0, 'нормальная масса тела')
        ]
    else:
        descriptions_of_bmi = [
            (13.5, 'недостаточная масса тела'),
            (18.0, 'нормальная масса тела')
        ]

    final_assessment = ''
    for number, text in descriptions_of_bmi:
        if bmi < number:
            final_assessment = text
            break
    if not final_assessment:
        final_assessment = ('ожирение 3-й степени'
                            if age >= 18
                            else 'избыточная масса тела')
    if age >= 18:
        return (f'\nСогласно рекомендациям ВОЗ, у Вас {final_assessment}.'
                '\nПодробнее об индексе массы тела: '
                'https://ru.wikipedia.org/wiki/Индекс_массы_тела')
    else:
        return (f'\nУ Вас {final_assessment}.'
                '\nВнимание! В Вашем возрасте организм ещё формируется, '
                'поэтому оценка может быть неточной.'
                '\nРекомендуется сверять индекс массы тела '
                'с региональными центильными таблицами у педиатров.')


def define_a_word_for_age(age):
    """Определение слова, которое будет напечатано в отчёте после возраста."""
    if 11 <= age % 100 <= 14:
        return 'лет'
    elif age % 10 == 1:
        return 'год'
    elif 2 <= age % 10 <= 4:
        return 'года'
    else:
        return 'лет'


print('Здравствуйте! Я бот FitLife.')
while True:
    user_name = input('Введите Ваше имя: ').strip()
    if user_name:
        break
    user_name = check_before_exiting_the_program('имя')
    break

user_age = enter_and_process_numerical_data(
    name_for_field='возраст',
    min_value=2,
    max_value=150,
    strict=False,
    range_error='Этот калькулятор предназначен для людей '
                'в возрасте от 2 до 150 лет! Пожалуйста, введите '
                'другое числовое значение возраста.',
    type_error='Некорректный ввод! Введите целое число (например, 25).',
    converter=int
)

user_weight = enter_and_process_numerical_data(
    name_for_field='вес',
    min_value=5,
    max_value=500,
    strict=True,
    range_error='Неверное значение! Введите реальный вес в килограммах '
                '(больше 5 и меньше 500 кг).',
    type_error='Некорректный ввод! Введите целое число (например, 45) '
                'или дробное, используя точку (например, 45.4).',
    converter=float
)

user_height = enter_and_process_numerical_data(
    name_for_field='рост',
    min_value=0.5,
    max_value=4,
    strict=True,
    range_error='Неверное значение! Введите реальный рост в метрах '
                '(больше 0.5 и меньше 4 м, например: 1.5, 1.75, 2).',
    type_error='Некорректный ввод! Введите значение в метрах '
                '(например: 1.5, 1.75, 2).',
    converter=float
)

# Расчёт индекса массы тела и его оценка.
body_mass_index = round(user_weight / (user_height ** 2), 1)
description_of_bmi = interpret_the_value_of_bmi(body_mass_index, user_age)

# Расчёт суточной нормы воды.
water_norm_in_ml = user_weight * WATER_PER_KG
water_norm_in_liters = round(water_norm_in_ml / ML_PER_LITER, 1)

# Печать отчёта.
word_for_age = define_a_word_for_age(user_age)
print(f'Отчёт для пользователя: {user_name} ({user_age} {word_for_age})')
print(f'\nВаш индекс массы тела: {body_mass_index}.')
print(f'{description_of_bmi}')
print(f'\nРекомендуемая норма воды: {water_norm_in_liters} л в день.')
print('\nРасчёт окончен. Будьте здоровы!')
