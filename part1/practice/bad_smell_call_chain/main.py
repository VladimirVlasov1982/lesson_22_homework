class Person:
    def __init__(self, room_num: int, city_population: int):
        self.room_num = room_num
        self.city_population = city_population

    def get_person_room(self):
        return self.room_num

    def get_city_population(self):
        return self.city_population


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

person = Person(42, 100500)

print(person.get_person_room())
print(person.get_city_population())
