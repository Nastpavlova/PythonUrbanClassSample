#Задача 4. Найти общие города среди двух групп и отсортировать их в алфавитном порядке.

fisrt_group = {"Москва", 'Владивосток', "Санкт-Петербург"}
second_group = {'Новосибирск', "Ижевск", "Санкт-Петербург", "Москва"}

same_city = fisrt_group.intersection(second_group) #set.intersection() - метод пересечения двух множеств

same_city = list (same_city) #мы делаем тип list, потому что до этого, если мы напишем print(type(same_city)) будет set - множество"""

same_city.sort() #сортируем города в алфавитном порядке

print(same_city)
