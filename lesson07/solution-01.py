#  Дан список стран и городов каждой страны, где ключи это названия стран,
#  а значения - списки городов в этих странах. Написать функцию которая осуществляет
#  поиск по городу и возвращает страну. Оформить в виде программы, которая считывает
#  название города и выводит на печать страну.

#  dictionary
countries = {
    "Belarus": ["Minsk", "Brest", "Grodno"],
    "Poland": ["Gdansk", "Warsaw", "Krakow"],
    "USA": ["Washington", "Chicago", "Boston"]
}

# request for city input
city = input("Enter the city name: ")

for key, value in countries.items():
    if value == city:
        print(key)
