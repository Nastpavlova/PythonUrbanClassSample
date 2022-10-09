class GreenZoneIndex:
    def __init__(self, territory_name, territory_area, green_zones):
        self.territory_name = territory_name
        self.territory_area = territory_area
        self.green_zones = green_zones
       
        self.green_index = self.calculate_green_index() # индекс озеленения

    def calculate_green_index(self):
        calculate_green_index = sum(self.green_zones) / self.territory_area * 100
        return round (calculate_green_index, 2)
 

territory1 = GreenZoneIndex ("Пушкин", 28676, [302, 487, 420, 325, 471, 363, 404])

print (f"Индекс озеленения территории {territory1.territory_name} равен {territory1.green_index} %")
