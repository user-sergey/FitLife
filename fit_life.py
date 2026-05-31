# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
ML_PER_LITER = 1000


def show_error_for_height_value():
    """Вывод ошибки при вводе роста > 4 м или вводе нечислового значения."""
    print('Некорректный ввод! Пожалуйста, введите значение в метрах '
          '(например: 1.5, 1.75, 2).')


print('Здравствуйте! Я бот FitLife.')
user_name = input('Напишите, пожалуйста, как Вас зовут? ').title()
while True:
    try:
        user_age = int(input('Ваш возраст? (вводите только число): '))
        break
    except ValueError:
        print('Некорректный ввод! '
              'Пожалуйста, введите целое число (например, 25).')

while True:
    try:
        user_weight = float(input('Введите Ваш вес (в кг): '))
        break
    except ValueError:
        print('Некорректный ввод! '
              'Пожалуйста, введите целое число (например, 45) '
              'или дробное, используя точку (например, 45.4).')

while True:
    try:
        user_height = float(input('Введите Ваш рост '
                                  '(в метрах, например, 1.62): '))
        if user_height > 4:
            show_error_for_height_value()
        else:
            break
    except ValueError:
        show_error_for_height_value()

# Расчёт индекса массы тела.
body_mass_index = round(user_weight / (user_height ** 2), 1)

# Расчёт суточной нормы воды.
water_norm_in_ml = user_weight * WATER_PER_KG
water_norm_in_liters = round(water_norm_in_ml / ML_PER_LITER, 1)

# Печать отчёта.
print(f'\nОтчёт для пользователя: {user_name} ({user_age} г.)')
print(f'Ваш индекс массы тела: {body_mass_index}')
print(f'Рекомендуемая норма воды: {water_norm_in_liters} л. в день.')
print('\nРасчёт окончен. Будьте здоровы!')
