# Чек

# Сдачу посчитать, конечно, все могут, но красивый чек напечатать — не так просто.
# Формат ввода

#     название товара;
#     цена товара;
#     вес товара;
#     количество денег у пользователя.

# Формат вывода

# Чек
# <название товара> - <вес>кг - <цена>руб/кг
# Итого: <итоговая стоимость>руб
# Внесено: <количество денег от пользователя>руб
# Сдача: <сдача>руб

name = str(input())
price = int(input())
weight = int(input())
money = int(input())
print(f"Чек\n{name} - {weight}кг - {price}руб/кг\n"
      f"Итого: {price * weight}руб\n"
      f"Внесено: {money}руб\n"
      f"Сдача: {money - (price * weight)}руб")


# Детский сад — штаны на лямках

# В продолжение темы детского сада давайте и там что-нибудь автоматизируем.
# За каждым ребёнком закреплён шкафчик и кровать. Номер шкафчика состоит из трёх цифр:

#     номер группы в саду;
#     номер кроватки, закреплённой за ребёнком;
#     порядковый номер ребёнка в списке группы.

# Воспитатель просит сделать программу, которая по имени ребенка и номеру его шкафчика формирует «красивую» карточку для личного дела.
# Формат ввода

# В первой строке записано имя ребенка.
# Во второй строке записан номер шкафчика.


name = str(input())
num = str(input())
print(f"Группа №{num[0]}.\n"
      f"{num[2]}. {name}.\n"
      f"Шкафчик: {num}.\n"
      f"Кроватка: {num[1]}.")


# Автоматизация игры

# Всё в том же детском саду ребята очень любят играть с цифрами.
# Одна из таких игр — перестановка цифр четырёхзначного числа.
# Напишите программу для робота-няни, которая из числа вида abcd составляет число badc.
# Формат ввода

# Одно четырёхзначное число.
# Формат вывода

# Одно четырёхзначное число — результат перестановки.


num = int(input())
print((num // 100) % 10, (num // 100) // 10, num % 10, (num % 100) // 10, sep="")


# Интересное сложение

# Один малыш из детского сада услышал от старшей сестры о некоем действии с числами — сложении.
# И как это часто бывает — он не до конца разобрался, как работает сложение. Например, не совсем понял, как произвести перенос разряда.
# Теперь он хочет научить сложению остальных ребят и просит написать программу, которая поможет ему в качестве наглядного материала.
# Формат ввода

# В первой и второй строках записаны натуральные числа меньше 1000.
# Формат вывода

# Одно число — результат сложения введённых чисел без учёта переносов.


num_1 = int(input())
num_2 = int(input())
print((((num_1 // 10) // 10) + (num_2 // 10) // 10) % 10,
      (((num_1 // 10) % 10) + ((num_2 // 10) % 10)) % 10,
      (num_1 % 10 + num_2 % 10) % 10, sep="")


# Шарики и ручки

# Иногда ребята в детском саду скучают, поэтому они постоянно придумывают себе не очень сложные, но веселые, по их мнению, игры.
# В группе есть ящик с шариками, количество которых детям заранее неизвестно, следующих цветов:

#     красный;
#     зеленый;
#     синий.

# Игра заключается в том, что каждый ребенок подходит к ящику и, не глядя, вытаскивает один шарик, победителем считается тот, кто первым вытащит зелёный шарик.
# Как вы думаете, через какое максимальное количество ходов дети выяснят победителя игры?
# Формат ввода

# Три натуральных числа, каждое на новой строке (количество красных, зеленых и синих шаров соответственно).
# Формат вывода

# Одно число — максимальное количество ходов, которое потребуется для определения победителя.


red = int(input())
green = int(input())
blue = int(input())
print((red + blue) + 1)


# В ожидании доставки

# Сегодня в N N часов M M минут хозяин магазина заказал доставку нового товара. Оператор сказал, что продукты доставят через T T минут.
# Сколько будет времени на электронных часах, когда привезут долгожданные продукты?
# Формат ввода

# В первой строке записано натуральное число N N ( 0 ≤ N < 24 0≤N<24).
# Во второй строке записано натуральное число M M ( 0 ≤ M < 60 0≤M<60).
# В третьей строке записано натуральное число T T ( 30 ≤ T < 1 0 9 30≤T<109).
# Формат вывода

# Одна строка, представляющая циферблат электронных часов.


n = int(input())
m = int(input())
t = int(input())
print(f'{((n + (t // 60)) % 24) + ((t % 60 + m) // 60):0>2}' + ":" + f'{(m + (t % 60)) % 60:0>2}')