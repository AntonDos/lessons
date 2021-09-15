#  Дан список словарей. Каждый словарь описывает машину (серийный номер, цвет и год выпуска).
#  Создать функцию, которая возвращает новый список со всеми машинами, год выпуска которых больше Х.

#  Написать декоратор, который будет выводить на печать время выполнения функции из предыдущей задачи
#  (end_time - start_time).

car_list = [
    {"sn": 4435, "color": "red", "year": 1999},
    {"sn": 6767, "color": "red", "year": 2007},
    {"sn": 8877, "color": "green", "year": 2005}
]


def filter_cars(year):
    result = []
    for car in car_list:
        if car["year"] > year:
            result.append(car)
    return result


def main():
    year = 2000
    filtered_cars = filter_cars(year)
    print(filtered_cars)


if __name__ == "__main__":
    main()
