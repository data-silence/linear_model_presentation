"""
    Создайте два банка: green_bank и red_bank
    Вызовите справочный метод default_info() для класса Client()
    Создайте объект student класса Client и определите его как клиента банка green_bank
    Создайте объект teacher класса Client и определите его как клиента банка red_bank
    Выведите справочную информацию о созданном объекте student (вызовите метод teacher.info())
    Выведите справочную информацию о созданном объекте teacher (вызовите метод print(teacher))
    Создайте объект класса SmallHouse
    Попробуйте для объекта student купить созданный дом, убедитесь в получении предупреждения
    Поправьте финансовое положение объекта student - вызовите метод earn_money()
    Снова попробуйте купить дом
    Посмотрите, как изменилось состояние объекта student
"""

from buy_house import *

green_bank = Bank()
red_bank = Bank()

Client.default_info()

student = Client(name='Вася Пупкин', age=18, bank=green_bank)
teacher = Client(name='Василий Пуповин', age=35, bank=red_bank)

teacher.info()
print(teacher)
sm_house = SmallHouse(price=10000)
# print(sm_house._price, sm_house._area)
student.buy_house(sm_house)
student.earn_money(15000)
print(student)
student.buy_house(sm_house)
print(student)
print(teacher)
bg_house = House(price=18_000, area=76)
teacher.buy_house(house=bg_house)
student.earn_money(7000)
print(student)
teacher.earn_money(20_000)
teacher.buy_house(bg_house)
print(teacher)
print(red_bank)
print(green_bank)
green_bank.add_account(student)
