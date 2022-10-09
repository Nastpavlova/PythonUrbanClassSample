#Задание 3. Написать функцию get_mean_green_index, которая в качестве аргумента принимает список объектов типа GreenZoneIndex и считает от них средний индекс озеленения.

class GreenZoneIndex:
    def __init__(self, territory_name, territory_area, green_zones):
        self.territory_name = territory_name
        self.territory_area = territory_area
        self.green_zones = green_zones
       
        self.green_index = self.calculate_green_index() # индекс озеленения

    def calculate_green_index(self):
        calculate_green_index = sum(self.green_zones) / self.territory_area * 100
        return round (calculate_green_index, 2)

list_territories = [
    {"territory_name": "Пушкин", "territory_area": 28676, "green_zones": [302, 487, 420, 325, 471, 363, 404]},
    {"territory_name": "Павловск", "territory_area": 21025, "green_zones": [360, 375, 223, 258, 345, 296, 303]},
    {"territory_name": "Петергоф", "territory_area": 44274, "green_zones": [364, 447, 438, 223, 336, 431, 442]}]

list1 = []

for city_information in list_territories:

  territory_name = city_information.get("territory_name") #Метод dict.get() возвращает значение для ключа key, если ключ находится в словаре.
  territory_area = city_information.get("territory_area")
  green_zones = city_information.get("green_zones")

  i = GreenZoneIndex(territory_name, territory_area, green_zones)

  list1.append(i.green_index)

def get_mean_green_index(wow):
    sr_znach = sum(wow) / len(wow)
    return round(sr_znach, 2)


def filter_min_green_index(list1, minimum = 0.1):

    list_green_index_min = []

    counter = 0
    for index in list1:
        if index < minimum:
            counter = counter + 1       
    return counter

#я удалила все print, которые выводили значения в предыдущих заданиях, потому что их было слишком много :(
print(f"Число территорий, индекс озеленения которых ниже 0.1 = {filter_min_green_index(list1)}.")