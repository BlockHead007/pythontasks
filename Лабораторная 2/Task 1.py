#Задание 1
##Списки
import math


def get_number():
    try:
        x = int(input("Введите количество посетителей: "))
        return x
    except:
        return 0


def output_string(x):
    print(f"Количество кусков: {x}")


def main():
    visitors = get_number()
    if visitors > 0:
        parts = 1
        visitors = visitors + math.ceil((visitors / 2)) + 10
        while parts < visitors:
            parts *= 2
        output_string(parts)
    else:
        print("Введено неверное число")


if __name__ == '__main__':
    main()