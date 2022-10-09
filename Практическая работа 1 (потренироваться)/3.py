#Задача 3. Отфильтровать города с населением больше 1 млн. человек.
list_cities = [{"name": "Москва","population": 12 * 10 ** 6}, {"name": "Санкт-Петербург","population": 5 * 10 ** 6}, {"name": "Ижевск","population": 0.6 * 10 ** 6}]


for city in list_cities:
    if city["population"] > 1000000:
        print (city)

