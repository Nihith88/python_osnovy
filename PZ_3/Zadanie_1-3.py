"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def simple_div():
    num_1 = float(input("Введите делимое:  "))
    num_2 = float(input("Введите делитель:  "))
    try:
        print(f" результат деления: {num_1 / num_2}")
    except ZeroDivisionError:  # в случае исключения "деление на ноль"
        print("Ошибка деления на ноль")  # выведем сообщение об ошибке
        simple_div()  # и рекурсивно вызовем функцию


# simple_div()

"""
2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, 
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. 
Осуществить вывод данных о пользователе одной строкой.
"""

def usr_data():
    f_name = input("Введите имя: ")
    l_name = input("Введите фамилию: ")
    year = input("Введите год вашего рождения: ")
    city = input("Введите город вашего проживания: ")
    mail = input("Введите email: ")
    phone = input("Введите номер телефона: ")
    print(f"Данные пользователя: {f_name} {l_name} {year} г.р. проживает в г.{city}, {mail} {phone}")

# usr_data()


"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента 
и возвращает сумму наибольших двух аргументов.
"""

def my_func():
    args = []
    args.append(int(input("Ведите первое число: ")))
    args.append(int(input("Ведите второе число: ")))
    args.append(int(input("Ведите третье число: ")))
    args.sort()
    return args[1] + args[2]

print(f"Сумма наибольших аргументов: {my_func()}")