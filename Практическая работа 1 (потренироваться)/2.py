#Задача 2. Сделать название городов с заглавной буквы.
list_cities = ["москва", "иЖЕВСк", "Владивосток", "новосибирсК", "мУРМАНСК"]
title_list_cities = [city.title() for city in list_cities] #операция title() (можно использовать capitalize()) - делает каждое слово в строке с заглавной буквы

new_list_cities = [] #создаём переменную

for city in title_list_cities: 
    new_list_cities.append(city) #метод append изменит список
    
print(new_list_cities)
