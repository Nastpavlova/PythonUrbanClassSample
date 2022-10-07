class homework:
    def __init__(self, grade: int, done:str, level:str, subject:str): #тут записали атрибуты для класса homework
        #далее мы присваиваем атрибутам значения аргументов конструктора объекта
        self.grade = grade #оценка за домашку
        self.done = done #выполнение домашки
        self.level = level #уровень сложности домашки (str потому что: легкий, средний и сложный)
        self.subject = subject #по какому предмету домашка

    def low_grade (self) -> int: 
        #функция уменьшает оценку на 1 балл, но если изначально оценка была <=2, то выводим оценку без изменения + "оценка итак низкая"
        #:return: Выводит текущую оценку

    def what_subject (self) -> str:
        #функция говорит по какому предмету домашка 
        #:return: предмет домашки

    def what_level (self) -> str:
        #функция выводит уровень сложности домашки
        #:return: уровень сложности домашки

class phone:
    def __init__ (self, brand: str, color: str, weight: int, price: int):
        self.brand = brand #бренд телефона
        self.color = color #цвет телефона
        self.weight = weight #вес телефона (int, потому что без грамм, просто в кг)
        self.price = price #цена телефона (int, потому что без копеек)

    def what_brend (self) -> str:
        #функция выводит бренд телефона
        #:return: бренд телефона

    def what_color (self) -> str:
        #функция выводит цвет телефона
        #:return: цвет телефона

    def weight_2 (self, phone_2_weight: int) -> int:
        #функция выводит вес двух телефонов
        #:param phone_2_weight: вес двух телефонов
        #:return: вес двух телефонов

class hostel:
    def __init__ (self, price:int, days:int, nights:int, stars:int):
        self.price = price #цена отеля за ночь
        self.days = days #количество дней в отеле
        self.nights = nights #количество ночей в отеле
        self.stars = stars #количество звёзд отеля

    def night_price (self, all_price:int) -> int:
        #функция выводит цену за проживание
        #:param all_price: цена за проживание определённое количество ночей
        #:return: выводит цену за проживание определённое количество ночей

    def how_night (self) -> int:
        #функция выводит сколько ночей проведено
        #:return: выводит количество ночей

    def how_days (self) -> int:
        #функция выводит сколько дней проведено
        #:return: выводит количество дней
