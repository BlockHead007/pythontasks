import math

def cons_input():
    try:
        a = float(input("Введите начало интегрирования: "))
        try:
            b = float(input("Введите конец интегрирования: "))
            try:
                eps = float(input("Введите точность вычисления: "))
                return a, b, eps
            except:
                print("Ошибка чтения")
                return 0, 0, 0
        except:
            print("Ошибка чтения")
            return 0, 0, 0
    except:
        print("Ошибка чтения")
        return 0, 0, 0


def integ(x: float) -> float:
    f = 5*x**4+2*x**3/3+(-7)*x+13
    return f


def task(a, b, eps):
    n = 1
    h = (b - a) / n
    s2 = integ(a + h*n) * h
    s1 = 0
    while math.fabs(s2-s1) <= eps:
        s1 = s2
        n *= 2
        h *= n
        s2 = 0
        x = a + b / 2
        for i in range(1, n):
            s2 = s2 + integ(x)
            x = x + h
        s2 = s2 * h
    return s2


def file_read():
    file = open("history.txt", "r+")
    print(file.read())
    file.close()


def file_write(a: float, b: float, eps: float, w: float):
    file = open("history.txt", "a+")
    file.write("a = " + str(a) + "; b = " + str(b) + "; eps = " + str(eps) + "; w = " + str(w) + "\n")
    file.close()


def cons_output(x):
    print(x)


def main():
    while True:
        print("Доступные функции:\n"
              "1. Посчитать интеграл\n"
              "2. Просмотреть историю\n"
              "0. Выход из программы\n")
        try:
            switch = int(input("Введите параметр: "))
        except:
            print("Ошибка чтения")
            continue
        match switch:
            case 0:
                break
            case 1:
                a, b, eps = cons_input()
                if a != 0 and b != 0 and eps != 0:
                    w = task(a, b, eps)
                    print(f"Полученный результат: {w}\n")
                    file_write(a, b, eps, w)
            case 2:
                file_read()
            case _:
                print("Неверная функция!")


if __name__ == '__main__':
    main()
    #3 функции: ввод, задание, вывод
    #меню: решить уравнение, история, выход