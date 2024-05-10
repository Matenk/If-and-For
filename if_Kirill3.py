# Задачи на if
# Задание №3
import time
color, color1 = input('Какие 2 цвета хотим смешать? ').split()
if color == 'красный' and color1 == 'синий' or color == 'синий' and color1 == 'красный':
    print('Мешаю цвета...')
    time.sleep(3)
    print('Мы получили фиолетовый цвет!')
elif color == 'красный' and color1 == 'жёлтый' or color == 'жёлтый' and color1 == 'красный':
    print('Мешаю цвета...')
    time.sleep(3)
    print('Мы получили оранжевый цвет!')
elif color == 'синий' and color1 == 'жёлтый' or color == 'жёлтый' and color1 == 'синий':
    print('Мешаю цвета...')
    time.sleep(3)
    print('Мы получили зелёный цвет!')
else:
    print('Мешаю цвета...')
    time.sleep(3)
    print('Ошибка! Вы ввели не тот цвет!')
