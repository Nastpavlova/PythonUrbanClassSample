# Задача. Написать класс City с 2 атрибутами и 1 методом.

class city:
    def __init__(self, name, population):
        self.name = name
        self.population = population
    
    def get_city_info (self):
        return (f"Город - {self.name}. Население = {self.population}.")

city1 = city('Иркутск', 654675)
city2 = city('Махачкала', 455272)


print(city1.name)
print(city2.get_city_info())


