#a) Создайте два списка в диапазоне (0, 100) с шагом 10. Присвойте некоторым переменным значения этих списков.
#b) Извлеките из первого списка второй элемент.
#c) Измените во втором списке последний объект на число «200». Выведите список на экран.
#d) Соедините оба списка в один, присвоив результат новой переменной.
#Выведите получившийся список на экран.
#e) Возьмите срез из соединённого списка так, чтобы туда попали некоторые части обоих первых списков. Срез свяжите с очередной новой переменной. Выведите значение этой переменной.
#f) Добавьте в список-срез два новых элемента и снова выведите его.
#g) С помощью функций min() и max() найдите и выведите элементы объединенного списка с максимальным и минимальным значением
import random

def task_a(size):
    list_new = []
    for i in range(size):
        t = random.randint(0, 100)
        list_new.append(t)
    return list_new


def task_b(list_task):
    list_task.pop(1)
    return list_task


def task_c(list_task):
    list_task.pop()
    list_task.append(200)
    return list_task


def task_d(list_task_1, list_task_2):
    list_combined = list_task_1 + list_task_2
    return list_combined


def task_e(list_combined):
    list_cutted = []
    i = 20
    while i < 40:
        list_cutted.append(list_combined[i])
        i += 1
    return list_cutted


def task_f(list_cutted):
    list_cutted.append(10)
    list_cutted.append(30)
    return list_cutted


def main():

    #Пункт a)
    list_1 = task_a(30)
    list_2 = task_a(25)
    print("Созданные списки:")
    print(list_1)
    print(list_2)
    print()

    #Пункт b)
    list1 = task_b(list_1)

    #Пункт c)
    list_2 = task_c(list_2)
    print("Видоизменённые списки:")
    print(list_1)
    print(list_2)
    print()

    #Пункт d)
    list_combined = task_d(list_1, list_2)
    print("Список после объединения:")
    print(list_combined)
    print()

    #Пункт e)
    list_cutted = task_e(list_combined)
    print("Обрезанный список:")
    print(list_cutted)
    print()

    #Пункт f)
    list_cutted = task_f(list_cutted)
    print("Обрезанный список после добавления элементов:")
    print(list_cutted)
    print()

    #Пункт g)
    print(f"Минимальный элемент в списке со срезом: {min(list_cutted)}")
    print(f"Максимальный элемент в списке со срезом: {max(list_cutted)}")

    return 0


if __name__ == '__main__':
    main()